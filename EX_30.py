import os
'''it is better to use dictionary methon to add new type of file, which is more universe '''
def count_filetype(path):

    file_num = 0
    txt_num = 0
    doc_num = 0
    docx_num = 0

    for each in os.listdir(path):
        print(os.path.splitext(each)[1])
        if os.path.splitext(each)[1] =='.docx':
            docx_num = docx_num + 1
        elif os.path.splitext(each)[1] == '':
            file_num = file_num + 1
        elif os.path.splitext(each)[1] == '.txt':
            txt_num = txt_num + 1
        elif os.path.splitext(each)[1] == '.doc':
            doc_num = doc_num + 1

    return file_num,txt_num,doc_num,docx_num

'''count every file size'''

def cal_file_size(path):
    for each in os.listdir(path):
        print("File Name:" + each + ", File Size:", end="")
        print(os.path.getsize(path + '\\' + each))


'''Find a file in a dirctory'''



if __name__ == '__main__':
    path = 'C:\\Users\\DELL\\Desktop\\Rent file\\Natashsa Info'
    # print(count_filetype(path))
    cal_file_size(path)










