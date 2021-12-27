import platform
import os

pmrep=False
pmcmd=False
infamcd=False

pmrep_app = 'pmrep.exe'
pmcmd_app = 'pmcmd.exe'
infacmd_app = 'infacmd.bat'

pmrepStatus=''
pmcmdStatus=''
pminfacmdStatus=''

installation_type=''

#print('Detailed platform string: {}'.format(platform.platform()))

# Not necessarily defined on Windows client
infa_home = os.getenv('INFA_HOME')

platform_system = platform.system()

print('')
print('  INFA_HOME    : {}'.format(infa_home))
print('  platform     : {}'.format(platform_system))
print('')
#print('pmserver file: {}'.format(os.path.exists(infa_home + '/server/bin/pmserver')))
#print('')

if(platform_system=='Linux'):
    pmrep_app = 'pmrep'
    pmcmd_app = 'pmcmd'
    infacmd_app = 'infacmd.sh'
    if(infa_home):
        if(os.path.exists(infa_home + '/server/bin/pmserver')):
            installation_type = 'server'
            infa_bin_path = infa_home + '/server/bin'
    else:
        installation_type = 'linux unknown'

elif(platform_system=='Windows'):
    # Could be Client or Server
    pmrep_app = 'pmrep.exe'
    pmcmd_app = 'pmcmd.exe'
    infacmd_app = 'infacmd.bat'
    # Check for INFA_HOME environment variable
    if(infa_home):
        # TODO: Need to confirm Windows server path
        if(os.path.exists(infa_home + '/server/bin/pmserver.exe')):
            installation_type = 'server'
            infa_bin_path = infa_home + '/server/bin'
        elif(os.path.exists(infa_home + '/clients/PowerCenterClient/CommandLineUtilities/PC/server/bin/pmcmd.exe')):
            installation_type = 'client'
            infa_bin_path = infa_home + '/clients/PowerCenterClient/CommandLineUtilities/PC/server/bin'
        else:
            installation_type = 'windows unknown'

else:
    installation_type = 'unknown [' + platform_system + ']'

# Check for tools
if(os.path.exists(infa_bin_path + '/' + pmrep_app)):
    pmrep = True
    pmrepStatus='Found'
if(os.path.exists(infa_bin_path + '/' + pmcmd_app)):
    pmcmd = True
    pmcmdStatus='Found'
if(os.path.exists(infa_bin_path + '/' + infacmd_app)):
    infacmd = True
    infacmdStatus='Found'

print('  bin path     : {}'.format(infa_bin_path))

print('  install type : {}'.format(installation_type))
print('')
print('  pmrep        : {}'.format(pmrepStatus))
print('  pmcmd        : {}'.format(pmcmdStatus))
print('  infacmd      : {}'.format(infacmdStatus))
