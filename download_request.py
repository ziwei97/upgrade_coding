import boto3
import os

import numpy as np
import pandas as pd
import random
import pathlib

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

#replace table name based on request
table_name = 'DFU_Master_ImageCollections'
table = dynamodb.Table(table_name)

#get attributes from dynamodb
def get_attribute(table,guid,attr):
    response = table.get_item(
        Key={
            'ImgCollGUID': guid
        }
    )
    # print(response)
    return response["Item"][attr]


def download_raw(table,raw_list,attrs):
    index=1
    fold = os.path.join("/Users/ziweishi/Documents", "dfu_pseudo_selected")
    # os.makedirs(fold)
    for i in raw_list:
        print(index)
        name = get_attribute(table,i,"Bucket")
        folder = os.path.join(fold, i)

        for j in attrs:
            try:
                attr = get_attribute(table,i,j)
                os.makedirs(folder)
                s = "PseudoColor/PseudoColor_"+str(i)+".tif"
                file_name= "PseudoColor_"+str(i)+".tif"
                file_path = os.path.join(folder, file_name)
                s3.Bucket(name).download_file(s, str(file_path))
                # for s in attr:
                #     print(type(s))
                #     file_name = s.split('/')[-1]
                #     if '.tif' not in file_name:
                #         file_name =file_name+".tif"
                #     print(file_name)
                #     file_path = os.path.join(folder, file_name)
                #     # s3.meta.client.download_file(name, attr[0], str(path))
                #     s3.Bucket(name).download_file(str(s), str(file_path))
            except Exception as e:
                error = str(i)+" "+str(j)
                print(error)
        index+=1



def replace_all(text,reo):
    for i in reo:
        if i in text:
            text.replace("i","")

    return text


data = pd.read_csv("/Users/ziweishi/Desktop/DFU/dfu_PseudoColor_list.csv")
list =data["ImgCollGUID"].to_list()

assess_list=[]
index=0
for i in list:
    print(index)
    try:
        ass = get_attribute(table,i,"PseudoColor")
        print(ass)
    except:
        assess_list.append(np.NAN)
    index+=1

#
# data_dfu = zip(list,assess_list)
# df = pd.DataFrame(data_dfu,columns=["guid","assessing"])
# df.to_excel("/Users/ziweishi/Desktop/DFU/dfu_list.xlsx")

# download_raw(table,list,attrs)