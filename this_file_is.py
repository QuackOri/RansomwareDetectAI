import sys
import os
from code import RDS
from code import BDS

if len(sys.argv) != 2:
  print("!!Please enter the directory name")
  print("ex) 'python this_file_is.py {directory_path}'")
  exit()

directory_path = sys.argv[1]
cwd = os.getcwd()

i = 0
for file in os.listdir(directory_path):
    file_path = directory_path+file

    # RDS
    api_result = RDS.is_ransom_by_api(cwd+'/models/r_api_model.pickle', file_path)
    sn_result = RDS.is_ransom_by_sectionname(cwd+'/models/r_new_sectionname_model.pickle', file_path)
    # BDS
    b_api_result = BDS.is_malware_by_api(cwd+'/models/b_api_model.pickle', file_path)
    b_etrp_result = BDS.is_malware_by_entropy(cwd+'/models/b_entropy_model.pickle', file_path)
    b_ep_result = BDS.is_malware_by_entrypoint(cwd+'/models/b_entrypoint_model.pickle', file_path)

    print("###", i, file, "###")
    print()
    if api_result[0] == 1:
        print('\033[31m' + "RDS-API: " + "Ransom" + '\033[0m')
    else:
        print('\033[32m' + "RDS-API: " + "It's okay" + '\033[0m')
    if sn_result[0] == 1:
        print('\033[31m' + "RDS-SN: " + "Ransom" + '\033[0m')
    else:
        print('\033[32m' + "RDS-SN: " + "It's okay" + '\033[0m')
    print()
    if b_api_result[0] == 1:
        print('\033[31m' + "BDS-API: " + "Malware" + '\033[0m')
    else:
        print('\033[32m' + "BDS-API: " + "It's okay" + '\033[0m')
    if b_etrp_result[0] == 1:
        print('\033[31m' + "BDS-ETRP: " + "Malware" + '\033[0m')
    else:
        print('\033[32m' + "BDS-ETRP: " + "It's okay" + '\033[0m')
    if b_ep_result[0] == 1:
        print('\033[31m' + "BDS-EP: " + "Malware" + '\033[0m')
    else:
        print('\033[32m' + "BDS-EP: " + "It's okay" + '\033[0m')
    
    print()

    if api_result[0] == 1 or sn_result[0] == 1:
        print("Stop! It's Ransom")
    elif b_api_result[0] == 1 or b_etrp_result[0] == 1 or b_ep_result[0] == 1:
        print("Warning! It's Malware")
    else:
        print("It's okay.. maybe")

    input()
    i+=1