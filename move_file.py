import os
import shutil

import pandas as pd

t_mask_path = "/Users/ziweishi/Documents/dfu_selected"
mask_path = "/Users/ziweishi/Documents/dfu_pseudo"
label_path = pd.read_excel("/Users/ziweishi/Desktop/pseudo.xlsx")
label = label_path["guid"].to_list()
print(label)
t_mask_list = os.listdir(mask_path)
if ".DS_Store" in t_mask_list:
    t_mask_list.remove(".DS_Store")

for i in t_mask_list:
    if i in label:
        t_guid_path = os.path.join(t_mask_path,i)
        guid_path =os.path.join(mask_path,i)
        os.mkdir(t_guid_path)
        file_list = os.listdir(guid_path)
        if ".DS_Store" in file_list:
            file_list.remove(".DS_Store")
        for h in file_list:
            file_path = os.path.join(guid_path,h)
            t_file_path = os.path.join(t_guid_path,h)
            shutil.copyfile(file_path, t_file_path)



#
#
# t_mask_list = os.listdir(t_mask_path)
# label_list1=os.listdir(label_path)
#
# if ".DS_Store" in t_mask_list:
#     t_mask_list.remove(".DS_Store")
#
# if ".DS_Store" in label_list1:
#     label_list1.remove(".DS_Store")
#
# label_list = [i for i in label_list1 if i in t_mask_list]
# print(len(label_list))
#
#
#
# for i in label_list:
#
#     file_path = os.path.join(label_path,i)
#     file_list = os.listdir(file_path)
#     if ".DS_Store" in file_list:
#         file_list.remove(".DS_Store")
#
#
#     for z in file_list:
#         print(type(z[0:5]))
#         if z[0:5]=="Final":
#             j="Label_"+z
#             print(j)
#             final_path = os.path.join(file_path,z)
#             target_path_guid = os.path.join(t_mask_path,i)
#             target_path = os.path.join(target_path_guid,j)
#             shutil.copyfile(final_path, target_path)
