import os
import pyinfa

infa_home=os.getenv('INFA_HOME')

print('INFA_HOME     : {}'.format(infa_home))

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
#print(retcode)
#print(version_details)

#powercenter command line get server versionprint(infa.ping('Domain', 'Repository_01', 'IntegrationService_01', '5'))

print(infa.startworkflow('Domain', 'IntegrationService_01', 'EXAMPLES', 'wf_Test', '5'))