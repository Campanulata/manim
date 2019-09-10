import os

f = open('run_manim.bat', 'w')

py_file_name = 'test.py'
classname = 'test1'
pl = ' -pl'
pm = ' -pm'
str01 = 'python3 -m manim' + py_file_name + ' ' + classname + pm

f.write(str01)
f.close()

os.system('run_manim.bat')
