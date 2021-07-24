python=open('E:\python\python.txt')
py = python.read()
print(py)
python.close()
with open('E:\python\python.txt') as the_file:
    print(the_file.mode)
