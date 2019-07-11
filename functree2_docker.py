## https://bioviz.tokyo/functree2/
import os , sys
import re

## configuration ##

sample_id = 'SRR000000'

description = '"test memo"' #Description of maximum 50 letters
modulecoverage = 0 #Compute module coverage = 1
private = 0 #Keep the result privatev  (Hide from "List of Profiles")= 1

root_file = '/tmp/'
pro_file = os.path.join(root_file,'profile.tsv')
profile_id = os.path.join(root_file,'profilr_id.txt')

series_list = ['mean','sum','modulecoverage']
series = series_list[0]

columns_list = ['sample1','sample2','sample3','sample4','sample5','sample6','sample7']
colums = ','.join(columns_list[0:2])

## mapping , get profile_id ##
cmd = "curl -X POST -H 'Accept: application/json' -H 'content-type: multipart/form-data' -o %s \
-F 'target=KEGG' \
-F 'description=%s' \
-F 'modulecoverage=%d' \
-F 'private=%d' \
-F 'input_file=@%s' \
https://bioviz.tokyo/functree2/api/mapping/" % (profile_id,description,modulecoverage,private,pro_file)
print(cmd)
os.system(cmd)


file = open(profile_id, 'r')
samplename = file.read()
prof_id = ','.join(re.findall(r'[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[[a-z0-9]{12}',samplename))
print(prof_id)

## download profile ##
cmd = "curl -X GET -H 'Accept: text/svg' \
'https://bioviz.tokyo/functree2/api/viewer/?profile_id=%s&series=%s&columns=%s' \
> %s%s.svg" %(prof_id,series,colums,root_file,sample_id)
print(cmd)
os.system(cmd)
