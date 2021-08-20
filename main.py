import xml.etree.ElementTree as ET
import xmltodict, json
import os
import glob
import pandas

TARGET_FILES = r'C:/Users/truongc/Dropbox/Cam_Karan/PYTHON/2001/*.xml'
file_list = glob.glob(TARGET_FILES)

# Python code to merge dict using update() method
def Merge(dict1, dict2):
    res = dict1 | dict2
    return res
meta_2001 ={}
x = 1

print(file_list)

for file in file_list:
    print(file)

    xml = ET.parse(file)
    myroot = xml.getroot()

    # Identity data
    data_info= {}
    for item in myroot:
        data_info[item.tag]=item.text
    print(data_info)

    data = {}
    #Main data
    for item in myroot[0]:
        data['headline'] = myroot[0][0].text
        data['body'] = myroot[0][1].text

    data_all = Merge(data_info, data)
    meta_2001[x] = data_all
    x += 1
print(meta_2001)
# jsonString = json.dumps(meta_2001)
# jsonFile = open("C:/Users/truongc/Dropbox/Cam_Karan/PYTHON/data2001.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()
df = pandas.DataFrame(meta_2001).T
print(df)
# df.to_csv('C:/Users/truongc/Dropbox/Cam_Karan/PYTHON/data2001.csv')