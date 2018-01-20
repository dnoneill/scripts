files = []
import urllib.request, os
import sys
import time
import datetime

output_path = input("Enter filepath to Download to: ")
list_of_files = input("Enter filename of list of files: ")
files_in_list = 0
with open(list_of_files) as file_text:
    for file in file_text:
        if file != "\n" and "mets" not in file:
            files.append(file.strip())
            files_in_list += 1
total = 0
for file in files:
    url, filename = file.split('masters/')
    #print(filename)
    total += 1
    urllib.request.urlretrieve(file, os.path.join(output_path, filename))
    sys.stdout.write("\rFiles done: %s/%s  Time Elapsed: %s" % (total, files_in_list, datetime.timedelta(seconds=int(time.clock())))) #writes number of files done, how much time has elapsed
    sys.stdout.flush()
    time.sleep(0.25)
print('{} files downloaded'.format(total))