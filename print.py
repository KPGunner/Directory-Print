import os
from time import sleep

pdf_mess = r'C:\Users\kgunn\Desktop\print test'
# pdf_mess = input('Copy and paste the folder path and hit enter.')

files = []
for filename in os.listdir(pdf_mess):
    files.append(filename)


lists = []
for name in files:
    lists.append(pdf_mess + '\\' + name)


list_length = len(lists)
attempt = 0

while attempt < list_length:
    for files_print in lists:
        os.startfile(files_print, 'print')
        sleep(10)
        print(f'Printed ---> {files_print} ')
        attempt += 1
