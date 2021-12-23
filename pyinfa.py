import subprocess

class pyinfa:
    def __init__(self, username, password):
        #self.domain_name = domain_name
        self.username = username
        self.password = password

        self.ignore_lines_version = (
            #'Informatica',
            'Copyright',
            'All Rights Reserved',
            'See patents',
            'This Software is protected',
            'Invoked at',
            'Completed at',
            'completed successfully',
            'Disconnecting',
            'ERROR:',
            'Command ran successfully',
            'List of',
            'Valid ',
            'Connected '
            )
        self.ignore_lines_general = self.ignore_lines_version + ('Informatica',)
        self._connected = False

    def format_output(self, command_output, processed_output, ignore_lines):
        #print(command_output)
        for line in command_output:
            #print(line)
            if line and not any(s in line for s in ignore_lines):
                # deduplicate as we go...
                if line not in processed_output:
                    #print('>>> {}'.format(line))
                    processed_output.append(line)

    def run_infa_command(self, command, ignore_lines, output):
        process = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            universal_newlines=True)

        raw_output = []
        print('--------------------')
        print('{} - {}'.format(command[0], command[1]))

        # Loop until command finished...
        while True:
            output_lines = process.stdout.readline()
            line = output_lines.strip()
            if line:
                #print('> ' + line)
                raw_output.append(line)

            # Check for a return code i.e. command complete
            return_code = process.poll()
            if return_code is not None:
                #print('>>> RETURN CODE: {}'.format(return_code))
                break
        
        # process the output
        self.format_output(raw_output, output, ignore_lines)
        
        return return_code



    def connect(self, domain_name, repository_svc_name):
        command = ['pmrep', 'connect', '-d', domain_name, '-r', repository_svc_name, '-n', self.username, '-x', self.password ]
        output=[]
        retcode = self.run_infa_command(command, self.ignore_lines_general, output)
        if(retcode == 0):
            self._connected = True
        return retcode

    def version(self, output):
        command = ['pmrep', 'version']
        temp = []
        retcode = self.run_infa_command(command, self.ignore_lines_version, temp)

        # Process the output
        for data in temp[0].split(', '):
            output.append(data)
        return retcode

    def ping(self, domain_name, repository_svc_name, integration_svc_name, timeout):
        command = ['pmcmd', 'pingservice', '-d', domain_name, '-sv', integration_svc_name, '-t', timeout ]
        output=[]
        #retcode = self.run_infa_command(command, self.ignore_lines_general, output)
        return self.run_infa_command(command, ('',''), output)

    def listfolders(self, output):
        if not(self._connected):
            return -1
        command = ['pmrep', 'listobjects', '-o', 'folder']
        #output=[]
        return self.run_infa_command(command, self.ignore_lines_general, output)

    def listworkflows(self, folder_name, output):
        if not(self._connected):
            return -1
        command = ['pmrep', 'listobjects', '-o', 'workflow', '-f', folder_name]
        temp=[]
        retcode = self.run_infa_command(command, self.ignore_lines_general, temp)

        # remove 'workflow ' from each entry
        prefix = 'workflow '
        for data in temp:
            if data.startswith(prefix):
                output.append(data[len(prefix):])
            else:
                output.append(data)

        return retcode

    def startworkflow(self, domain_name, integration_svc_name, folder_name, workflow_name, timeout):
        command = ['pmcmd', 'startworkflow', '-d', domain_name, '-sv', integration_svc_name, '-u', self.username, '-p', self.password, '-t', timeout, '-f', folder_name, '-wait', workflow_name ]
        output=[]
        #retcode = self.run_infa_command(command, self.ignore_lines_general, output)
        return self.run_infa_command(command, ('',''), output)