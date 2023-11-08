import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+'\\codes')

from codes import RDS
from codes import BDS

if len(sys.argv) != 2:
    exit()

directory_path = sys.argv[1]

ransom_path = os.path.join(directory_path, "Ransom")
malware_path = os.path.join(directory_path, "Malware")
normal_path = os.path.join(directory_path, "normal")

total_ransom = os.listdir(ransom_path)
total_malware = os.listdir(malware_path)
total_normal = os.listdir(normal_path)

# [correct, false]
r_api_score = [0, 0]
r_sn_score = [0, 0]
r_pe_score = [0, 0]
b_api_score = [0, 0]
b_etrp_score = [0, 0]
b_ep_score = [0, 0]

# detect
r_api_detect = 0
r_sn_detect = 0
r_pe_detect = 0

# entire
entire_ransom = 0
entire_malware = 0
entire_normal = 0

# Ransom
for file in os.listdir(ransom_path):
    file_path = os.path.join(ransom_path, file)
    
    # RDS
    r_api_result = RDS.is_ransom_by_api(cwd+'/models/r_api_model.pickle', file_path)
    if r_api_result[0] == 1:
        r_api_score[0] += 1
        r_api_detect += 1
    else:
        r_api_score[1] += 1
    r_sn_result = RDS.is_ransom_by_sectionname(cwd+'/models/r_new_sectionname_model.pickle', file_path)
    if r_sn_result[0] == 1:
        r_sn_score[0] += 1
        r_sn_detect += 1
    else:
        r_sn_score[1] += 1
    r_pe_result = RDS.is_ransom_by_pe(cwd+'/models/r_pe_model.pickle', file_path)
    if r_pe_result[0] == 1:
        r_pe_score[0] += 1
        r_pe_detect += 1
    else:
        r_pe_score[1] += 1
    # BDS
    b_api_result = BDS.is_malware_by_api(cwd+'/models/b_api_model.pickle', file_path)
    if b_api_result[0] == 1:
        b_api_score[0] += 1
    else:
        b_api_score[1] += 1
    b_etrp_result = BDS.is_malware_by_entropy(cwd+'/models/b_entropy_model.pickle', file_path)
    if b_etrp_result[0] == 1:
        b_etrp_score[0] += 1
    else:
        b_etrp_score[1] += 1
    b_ep_result = BDS.is_malware_by_entrypoint(cwd+'/models/b_entrypoint_model.pickle', file_path)
    if b_ep_result[0] == 1:
        b_ep_score[0] += 1
    else:
        b_ep_score[1] += 1

    if r_api_result[0] + r_sn_result[0] == 2 or r_pe_result[0] == 1:
        entire_ransom += 1
    elif r_pe_result[0] == 0 and r_api_result[0] + r_sn_result[0] == 1 :
        entire_malware += 1
    elif (b_api_result[0] + b_etrp_result[0] == 1 + b_ep_result[0] == 1) > 1 :
        entire_malware += 1
    else:
        entire_normal += 1

# Malware
for file in os.listdir(malware_path):
    file_path = os.path.join(malware_path, file)
    
    # RDS
    r_api_result = RDS.is_ransom_by_api(cwd+'/models/r_api_model.pickle', file_path)
    if r_api_result[0] == 0:
        r_api_score[0] += 1
    else:
        r_api_score[1] += 1
    r_sn_result = RDS.is_ransom_by_sectionname(cwd+'/models/r_new_sectionname_model.pickle', file_path)
    if r_sn_result[0] == 0:
        r_sn_score[0] += 1
    else:
        r_sn_score[1] += 1
    r_pe_result = RDS.is_ransom_by_pe(cwd+'/models/r_pe_model.pickle', file_path)
    if r_pe_result[0] == 0:
        r_pe_score[0] += 1
    else:
        r_pe_score[1] += 1
    # BDS
    b_api_result = BDS.is_malware_by_api(cwd+'/models/b_api_model.pickle', file_path)
    if b_api_result[0] == 1:
        b_api_score[0] += 1
    else:
        b_api_score[1] += 1
    b_etrp_result = BDS.is_malware_by_entropy(cwd+'/models/b_entropy_model.pickle', file_path)
    if b_etrp_result[0] == 1:
        b_etrp_score[0] += 1
    else:
        b_etrp_score[1] += 1
    b_ep_result = BDS.is_malware_by_entrypoint(cwd+'/models/b_entrypoint_model.pickle', file_path)
    if b_ep_result[0] == 1:
        b_ep_score[0] += 1
    else:
        b_ep_score[1] += 1

    if r_api_result[0] + r_sn_result[0] == 2 or r_pe_result[0] == 1:
        entire_ransom += 1
    elif r_pe_result[0] == 0 and r_api_result[0] + r_sn_result[0] == 1 :
        entire_malware += 1
    elif (b_api_result[0] + b_etrp_result[0] == 1 + b_ep_result[0] == 1) > 1 :
        entire_malware += 1
    else:
        entire_normal += 1

# Normal
for file in os.listdir(normal_path):
    file_path = os.path.join(normal_path, file)
    
    # RDS
    r_api_result = RDS.is_ransom_by_api(cwd+'/models/r_api_model.pickle', file_path)
    if r_api_result[0] == 0:
        r_api_score[0] += 1
    else:
        r_api_score[1] += 1
    r_sn_result = RDS.is_ransom_by_sectionname(cwd+'/models/r_new_sectionname_model.pickle', file_path)
    if r_sn_result[0] == 0:
        r_sn_score[0] += 1
    else:
        r_sn_score[1] += 1
    r_pe_result = RDS.is_ransom_by_pe(cwd+'/models/r_pe_model.pickle', file_path)
    if r_pe_result[0] == 0:
        r_pe_score[0] += 1
    else:
        r_pe_score[1] += 1
    # BDS
    b_api_result = BDS.is_malware_by_api(cwd+'/models/b_api_model.pickle', file_path)
    if b_api_result[0] == 0:
        b_api_score[0] += 1
    else:
        b_api_score[1] += 1
    b_etrp_result = BDS.is_malware_by_entropy(cwd+'/models/b_entropy_model.pickle', file_path)
    if b_etrp_result[0] == 0:
        b_etrp_score[0] += 1
    else:
        b_etrp_score[1] += 1
    b_ep_result = BDS.is_malware_by_entrypoint(cwd+'/models/b_entrypoint_model.pickle', file_path)
    if b_ep_result[0] == 0:
        b_ep_score[0] += 1
    else:
        b_ep_score[1] += 1

    if r_api_result[0] + r_sn_result[0] == 2 or r_pe_result[0] == 1:
        entire_ransom += 1
    elif r_pe_result[0] == 0 and r_api_result[0] + r_sn_result[0] == 1 :
        entire_malware += 1
    elif (b_api_result[0] + b_etrp_result[0] == 1 + b_ep_result[0] == 1) > 1 :
        entire_malware += 1
    else:
        entire_normal += 1

total = total_malware+total_ransom+total_normal

print("# RDS-API ")
print("correct ( ", r_api_score[0],"/",total,")")
print("detect (", r_api_detect, "/", total_ransom, ")")
print("# RDS-SN ")
print("correct ( ", r_sn_score[0],"/",total,")")
print("detect (", r_sn_detect, "/", total_ransom, ")")
print("# RDS-PE ")
print("correct ( ", r_pe_score[0],"/",total,")")
print("detect (", r_pe_detect, "/", total_ransom, ")")
print("# BDS-API ")
print("correct ( ", b_api_score[0],"/",total,")")
print("# BDS-ETRP ")
print("correct ( ", b_etrp_score[0],"/",total,")")
print("# BDS-EP ")
print("correct ( ", b_ep_score[0],"/",total,")")

print("entire ransom ( ", entire_ransom, '/', total_ransom, ')')
print("entire malware ( ", entire_malware, '/', total_malware, ')')
print("entire normal ( ", entire_normal, '/', total_normal, ')')
