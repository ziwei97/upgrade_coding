import logging
import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.resource('s3')


# def upload_file(file_name, bucket, object_name=None):
#     """Upload a file to an S3 bucket
#
#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """
#
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)
#
#     # Upload the file
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True


folder_path = "/Users/ziweishi/Documents/dfu_pseudo_selected"
folder=os.listdir(folder_path)


index=0
for i in folder:
    if ".DS_Store" not in i:
        print(index)
        guid_path=os.path.join(folder_path,i)
        file_list=os.listdir(guid_path)
        for j in file_list:
            if ".DS_Store" not in j:
                file_path = os.path.join(guid_path,j)
                print(file_path)
                file_name = "DataScience/DFU_SSP_WAUSI_Data_2023-03-23/"+i+"/"+j
                s3.Bucket("spectralmd-datashare").upload_file(file_path,file_name )
        index+=1
