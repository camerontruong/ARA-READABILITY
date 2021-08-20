import time
import zipfile
from pyexpat import ExpatError
from zipfile import ZipFile
import xmltodict, json
import os
import glob

YEAR = 2004

while True:
    TARGET_FILES = f'C:/Users/truongc/Dropbox/Cam_Karan/PYTHON/{YEAR}/*.xml'
    file_list = glob.glob(TARGET_FILES)
    print(len(file_list))
    time.sleep(5)
# meta = {}
# for file in file_list:
#     print(file)
#     try:
#         with open(file, 'r', encoding='utf-8') as file:
#             obs = xmltodict.parse(file.read())
#         meta[str(file)] = obs
#     except ExpatError:
#         print('some error')
#
#
# jsonString = json.dumps(meta,indent=4)
# # print(jsonString)
#
# # zipf = ZipFile("2001.zip", "w")
# # zipf.write(jsonString)
# #
# # zipf.close()
#
# jsonFile = open(r"C:/Users/truongc/Dropbox/Cam_Karan/PYTHON/StreetEvent/data_2004.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()
# print(f"{len(file_list)} transcripts written in the Json file")



# with open(r'C:\Users\truongc\Dropbox\Cam_Karan\PYTHON', 'w') as outfile:
#         json.dump(meta_2001, outfile)

# print(meta_2001json)
# print(obs["Event"]["EventStory"]["Body"])