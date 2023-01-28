import os #To communicate with os
import time


class FileFinder:
    def __init__(self):
        pass
    def find_file(self,filename,filepath):
        files=[]
        self.filename=filename
        self.filepath=filepath
        for root,dir,file in os.walk(filepath):# walk()it give 3 information details(root,dir,file)
            if filename in file:
                files.append(os.path.join(root,filename))
        return files
if __name__ == '__main__':
   # obj=FileFinder()
   # print(obj.find_file('Sql file 1.txt', 'C:/HCL1'))
   st=time.time()
   obj=FileFinder()
   print(obj.find_file('Sql file 1.txt','C:/'))
   et=time.time()
   print(et-st)




