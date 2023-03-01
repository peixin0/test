'''
build a file on python, name the file and write content raw by raw.
'''


file_name = ""
content = ""

def build_file():
    print("plz enter your txt file name:")
    file_name = input ()
    print("plz enter the content:")
    f = open ('E:\PYEX\\'+file_name+".txt",'w')
    while True:
        content = input()

        if content == "exit":
            break
        else:
            f.write(content)
    f.close()


build_file()



