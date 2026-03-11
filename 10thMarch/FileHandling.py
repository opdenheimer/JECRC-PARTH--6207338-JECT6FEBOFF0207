#filehandling

'''
file is a type of container containing some data and to handle that or apply operations on it like read,write 
execute is called file handling and now to know which type of that file is done by checking the extension of file 
.py,.mp4.html,.mp3

to open that file we have open ()
open('filename.ext'/'absolute_path,mode)

close():
  var_name.close()

  here we have 3 different operation to do on a file 
  read (r)
  write(w)
  append(a)

  write mode:
  only write(w)
  write+read(w+)
  write binary(wb)
  write & read binary(wb+)

  read mode:
  only read(r)
  write+read(r+)
  read Binary(rb)
  read & write binary(rb+)

  append mode:
  only append
  append+ read(a+)
  append binary(ab)
  append & read binary(ab+)
'''
# read 

file=open("temp.txt",'w+')
# print(file.read())
# print(file.readline())
file.writelines([
    'firstline\n',
    'SecondLine\n',
    'thirdline\n',

])
file.seek(0)
print(file.read())
file.close()


