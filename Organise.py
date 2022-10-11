import os
import shutil

fromDir = "C:/Users/JOY/OneDrive/Desktop/PDF"

toDir = "C:/Users/JOY/OneDrive/Desktop/School"

list_of_files= os.listdir(fromDir)
#print(list_of_files)

for file_name in list_of_files:
   # print(file_name)

   name,extension = os.path.splitext(file_name)
#    print(name)
#    print(extension)
   if (extension == ""):
        continue
   if extension in ['.pdf','.doc','.txt']:

        path1=fromDir+'/'+file_name

        path2 = toDir+'/'+"newDocFolder"

        path3= toDir+'/'+"newDocFolder"+"/"+file_name

        if os.path.exists(path2):
            print("moving files....")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving files....")
            shutil.move(path1,path3)

