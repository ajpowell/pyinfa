import logging
import os
import pyinfa

logging.root.handlers = []
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    #datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
    )

def main():   
    infa_home=os.getenv('INFA_HOME')
    logging.info('INFA_HOME     : {}'.format(infa_home))

    infa = pyinfa.pyinfa('cmd_user', 'cmd_user_password')

    #infa.connect('Domain', 'Repository_01')

    #folder_list = []
    #infa.listfolders(folder_list)
    #print(folder_list)

    #workflow_list = []
    #infa.listworkflows(folder_name='EXAMPLES', output=workflow_list)
    #print(workflow_list)

    #version_details = []
    #retcode = infa.version(version_details)
    #logging.debug(retcode)
    #logging.info(version_details)

    #print(infa.ping('Domain', 'Repository_01', 'IntegrationService_01', 5))

    #print(infa.startworkflow('Domain', 'IntegrationService_01', 'EXAMPLES', 'wf_Test', 5))

    '''
    # probe the system...this takes some time...
    service_list=[]
    services = [
        ['AS','Analyst Service'], 
        #['BW','PowerCenter SAP BW Service'], # Problem with this code despite being listed in the help 
        ['CMS','Content Management Service'], 
        ['DIS','Data Integration Service'], 
        ['IS','PowerCenter Integration Service'], 
        ['MM','Metadata Manager Service'], 
        ['MRS','Model Repository Service'], 
        #['RPS',''], # Unknown 
        ['RS','PowerCenter Repository Service'], 
        ['WS','Web Services Hub'], 
        #['ES',''], # Unknown 
        ['SCH','Scheduler Service'], 
        ['RMS','Resource Manager Service'], 
        ['SEARCH','Search Service']
        ]
    # iterate through all the services
    for service_code, service in services:
        output = []
        # Valid service types AS|BW|CMS|DIS|IS|MM|MRS|RPS|RS|WS|ES|SCH|RMS|SEARCH
        if(infa.listservices('Domain', service_code, 5, output)==0):
            for item in output:
                service_list.append(item)

    print(service_list)
    '''
    
    '''
    output = []
    infa.listnodes('Domain', 5, output)

    print(output)
    '''

    licences = []
    licence_details=[]
    #infa.listlicenses('Domain', 5, licences)
    #for licence in licences:
    #    print(licence)
    #    infa.showlicense('Domain',licence, '5', licence_details)
    infa.showlicense('Domain','10.1.0_License_localhost.localdomain_136933', 5, licence_details)
    print(licence_details)



    

if __name__ == '__main__':
    main()
