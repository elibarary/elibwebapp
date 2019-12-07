import os
import csv

d = r"/home/u/Downloads"

lists = []
for path in os.listdir(d):
    
    full_path = os.path.basename(path)
    
    pathplus = "allfiles/"+full_path
    print(pathplus)
    lists.append(pathplus)



print(lists)
RE = [lists]
with open('outpu.csv','w') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerow(lists)
