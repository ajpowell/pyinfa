'''
test_parse_userDetails.py


'''

import pyinfa
import datetime

infa = pyinfa.pyinfa('infa_username', 'infa_password')

def test_parse_UserDetails():
    message = 'User Administrator using application Integration Service (pmserver) on host localhost (127.0.0.1), port 33096, logged in successfully.'
    
    # ts = int(log_entry['@timestamp'])/1000
    ts = 1640621393.667 # 2021-12-27 16:09:48,785
 
    logintime = datetime.datetime.fromtimestamp(ts)
    # print(infa.parse_userDetails(message, logintime))
    assert infa.parse_userDetails(message, logintime) == {'port': '33096', 'time': '2021-12-27 16:09:53.667000', 'user': 'Administrator', 'application': 'Integration Service (pmserver)', 'hostname': 'localhost (127.0.0.1)'}