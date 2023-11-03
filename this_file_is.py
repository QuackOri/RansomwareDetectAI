import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+'\\codes')

from codes import RDS
from codes import BDS

if len(sys.argv) != 2:
  print("!!Please enter the directory name")
  print("ex) 'python this_file_is.py {directory_path}'")
  exit()

directory_path = sys.argv[1]

i = 0
for file in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file)

    # RDS
    api_result = RDS.is_ransom_by_api(cwd+'/models/r_api_model.pickle', file_path)
    sn_result = RDS.is_ransom_by_sectionname(cwd+'/models/r_new_sectionname_model.pickle', file_path)
    pe_result = RDS.is_ransom_by_pe(cwd+'/models/r_pe_model.pickle', file_path)
    # BDS
    b_api_result = BDS.is_malware_by_api(cwd+'/models/b_api_model.pickle', file_path)
    b_etrp_result = BDS.is_malware_by_entropy(cwd+'/models/b_entropy_model.pickle', file_path)
    b_ep_result = BDS.is_malware_by_entrypoint(cwd+'/models/b_entrypoint_model.pickle', file_path)

    # cls
    clear = lambda : os.system('cls')
    clear()
  
    print("###", i, file, "###")
    print()
    if api_result[0] == 1:
        print('\033[31m' + "RDS-API: " + "Ransom" + '\033[0m')
    else:
        print('\033[32m' + "RDS-API: " + "No Ransom" + '\033[0m')
    if sn_result[0] == 1:
        print('\033[31m' + "RDS-SN: " + "Ransom" + '\033[0m')
    else:
        print('\033[32m' + "RDS-SN: " + "No Ransom" + '\033[0m')
    if pe_result[0] == 1:
        print('\033[31m' + "RDS-PE: " + "Ransom" + '\033[0m')
    else:
        print('\033[32m' + "RDS-PE: " + "No Ransom" + '\033[0m')
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

    if api_result[0] + sn_result[0] == 2 or pe_result[0] == 1:
        print("Stop! It's "+'\033[31m'+"Dangerous"+ '\033[0m')
    elif pe_result[0] == 0 and api_result[0] + sn_result[0] == 1 :
        print('\033[33m'+"Warning!Warning!!Warning!!!"+'\033[0m')
    elif (b_api_result[0] + b_etrp_result[0] == 1 + b_ep_result[0] == 1) > 1 :
        print('\033[33m'+"Warning!Warning!!Warning!!!"+'\033[0m')
    else:
        print("It's "+'\033[32m' + "okay.."+'\033[0m'+" maybe")

    input()
    i+=1
