import logging
import os
import sys
import pyinfa
import datetime
import json

domain_name='Domain_DEV'
repository_service='RepositoryService_01'
integration_service='IntegrationService_01'

infa_username='Administrator'
infa_password='5uB7BvycgyVK'

logging.root.handlers = []
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    #datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
    #level=logging.DEBUG
    )

def main():   
    infa_home=os.getenv('INFA_HOME')
    logging.info('INFA_HOME     : {}'.format(infa_home))

    infa = pyinfa.pyinfa(infa_username, infa_password)

    infa.connect(domain_name, repository_service)

    '''
    print('\nFolder list')
    folder_list = []
    infa.listfolders(folder_list)
    print(folder_list)

    print('\n')

    for folder in folder_list:
        workflow_list = []
        logging.info(folder)
        infa.listworkflows(folder, workflow_list)
        print(workflow_list)

    '''

    # sys.exit(1)

    #version_details = []
    #retcode = infa.version(version_details)
    #logging.debug(retcode)
    #logging.info(version_details)

    #sys.exit(1)

    #print(infa.ping(domain_name, repository_service, integration_service, 5))

    #sys.exit(1)

    #print(infa.startworkflow(domain_name, integration_service, 'EXAMPLES', 'wf_Test', 5))

    '''
    # probe the system...this takes some time...
    service_list=[]
    services = [
        ['AS','Analyst Service'], 
        #['BW','SAP BW Service'], # Problem with this code despite being listed in the help 
        ['CMS','Content Management Service'], 
        ['DIS','Data Integration Service'], 
        ['IS','PowerCenter Integration Service'], 
        ['MM','Metadata Manager Service'], 
        ['MRS','Model Repository Service'], 
        ['RPS','Reporting Service'],
        ['RS','PowerCenter Repository Service'], 
        ['WS','Web Services Hub'], 
        ['ES','Email Service'], 
        ['SCH','Scheduler Service'], 
        ['RMS','Resource Manager Service'], 
        ['SEARCH','Search Service']
        ]
    # iterate through all the services
    for service_code, service in services:
        output = []
        # Valid service types AS|BW|CMS|DIS|IS|MM|MRS|RPS|RS|WS|ES|SCH|RMS|SEARCH
        if(infa.listservices(domain_name, service_code, 5, output)==0):
            for item in output:
                service_list.append(item)

    print(service_list)
    '''
    '''
    print('\nNode list')
    output = []
    infa.listnodes(domain_name, 5, output)

    print(output)

    print('\nLicence List')
    licences = []
    licence_details=[]
    infa.listlicenses(domain_name, 5, licences)
    for licence in licences:
        print(licence)
        infa.showlicense(domain_name,licence, '5', licence_details)
    #infa.showlicense('Domain_DEV','10.1.0_License_localhost.localdomain_136933', 5, licence_details)
    #print(licence_details)
    
    sys.exit(1)

    '''
    
    output = []
    infa.getLog(domain_name, 'RS', 5, output)
    #print('\n\n==============================================================')
    full_xml = ''
    for entry in output:
        # Handle poor XML generation (logEvent tags not closed correctly)
        if entry != '</logEvent>': # Ignore if closure on it's own
            if entry == '</logEvent></log>': # remove spurious closure
                full_xml = full_xml + '</log>'
            else:
                full_xml=full_xml + entry

            if '<logEvent' in entry:
                # if logEvent not closed, then close it
                if entry.find('</logEvent>')==-1:
                    full_xml=full_xml + '</logEvent>'
            
            full_xml=full_xml + '\r'

    #    if 'REP_51002' in entry: # Startup of repository
    #        print(entry)
    #    if 'CNX_53032' in entry: # User login
    #        if entry.find('pmserver')==-1: # Ignore pmserver rows
    #            if entry.find('application  on')==-1: # Ignore unknown applications
    #                print(entry)

    #print(full_xml)
    #print('\n\n')
    
    
    
    import xmltodict    
    # Convert the xml to a dictionary   
    dict_data = xmltodict.parse(full_xml)
    # Convert dictionary to json string
    string_json = json.dumps(dict_data)
    # Convert the json string to a json object
    obj_json = json.loads(string_json)

    #print('\n==============================================================\n')
    #print(obj_json)
    
    for log_entry in obj_json['log']['logEvent']:
        if log_entry['@messageCode']=='CNX_53032':
            #print(log_entry)
            #print('')
            ts = int(log_entry['@timestamp'])/1000
            full_datetime = datetime.datetime.fromtimestamp(ts)
            #print(full_datetime)
            #print(log_entry['@message'])
            # Parse out details from @message
            login_details = infa.parse_userDetails(log_entry['@message'], full_datetime)
            #print('-------------------------------------')
            #print(login_details)
            #if (login_details['application'] != 'AdminConsole' and 
            #    login_details['application'] != 'Integration Service (pmserver)' and 
            #    login_details['application'] != ''):
            if login_details['application'] not in ['AdminConsole', 'pmrep', 'Integration Service (pmserver)','']:
                print(login_details)
            #print('-------------------------------------')
    
    '''
    for log_entry in obj_json['log']['logEvent']:
        if log_entry['@messageCode']=='CNX_53032':
            #print(log_entry)
            # Ignore logins for pmserver (internal)
            if log_entry['@message'].find('(pmserver')==-1:
                if log_entry['@message'].find('application  on')==-1:
                    ts = int(log_entry['@timestamp'])/1000
                    full_datetime = datetime.datetime.fromtimestamp(ts)
                    print(full_datetime)
                    print(log_entry['@message'])
                    print('-------------------------------------')
    '''
    '''
    # Untangle timestamps listed in XML log output
    import datetime
    ts = 1640621393667 # Timestamp form XML ~ 2021-12-27 16:09:48,785
    ts = 1640621393.667 # 2021-12-27 16:09:48,785
    datetime = datetime.datetime.fromtimestamp(ts)
    print(datetime)
    '''


if __name__ == '__main__':
    main()
    #parse_userDetails('User Administrator using application Integration Service (pmserver) on host localhost (127.0.0.1), port 33096, logged in successfully.')
