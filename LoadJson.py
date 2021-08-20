import xmltodict, json


with open(r"C:\Users\truongc\Dropbox\Cam_Karan\PYTHON\StreetEvent\data_2001.json", "r") as file:
    data = json.loads(file.read())


print(data)
