import os
import pandas as pd

# aws s3 ls s3://spectralmd-datashare/DataScience/MSI_Generation_Phase_III_2023-03-14/ --recursive | cat >> /Users/ziweishi/Desktop/s3_list.txt



path = "/Users/ziweishi/Desktop/S3_list.xlsx"
df = pd.read_excel(path,sheet_name="Sheet1")
# list = pd.read_excel(path,sheet_name="subjectid")
# guid=list["list_id"].to_list()
df1 = pd.read_excel(path,sheet_name="Sheet2")
guid = df1["imguid"].to_list()


raw = []
assess =[]
pseudo = []
p=1
for i in guid:
    subset = df[df["guid"]==i]
    file_list = subset["file"].to_list()
    pseudo_num = 0
    raw_num = 0
    ass_num = 0
    for j in file_list:
        if j[0:3] =="Pse" and j[-1]=="f":
            pseudo_num+=1
        if j[0:3] =="Raw" and j[-1]=="f":
            raw_num+=1
        if j[0:3] =="Ass":
            ass_num+=1

    pseudo.append(pseudo_num)
    assess.append(ass_num)
    raw.append(raw_num)
    print(p)
    p+=1

final = zip(guid,pseudo,assess,raw)


data = pd.DataFrame(final,columns=["guid","pseudo_num","assess_num","raw_num"])
data.to_excel("/Users/ziweishi/Desktop/wasp_msi_s3_checking.xlsx")