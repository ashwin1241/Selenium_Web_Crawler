import shutil
import os


def fn(name1, f):
    f1 = False
    name = ''
    for line in f:
        line1 = line.split(' ')
        for word in line1:
            if word == name1:
                f1 = True
                continue
            if f1:
                name = word
                break
        if f1:
            break
    return name


src_path = ' '
while src_path == ' ':
    srno = 1
    srno = int(input("Enter the SrNo. of the file to test:\n\n1) irctc-user-1.side\n2) irctc-user-2.side\n3) makemytrip-user-1.side\n4) makemytrip-user-2.side\n5) yatra-user-1.side\n6) yatra-user-2.side\n\n"))
    if srno == 1:
        src_path = './irctc-user-1.side'

    elif srno == 2:
        src_path = './irctc-user-2.side'

    elif srno == 3:
        src_path = './makemytrip-user-1.side'

    elif srno == 4:
        src_path = './makemytrip-user-2.side'

    elif srno == 5:
        src_path = './yatra-user-1.side'

    elif srno == 6:
        src_path = './yatra-user-2.side'

    else:
        print("\nInvalid input, try again.\n")


# src_path = input('Enter a source file path: ')
if os.path.exists(src_path):
    print("\n")

    # print('The file exists, executing script...')

    fp = open('temp.txt', 'w')
    fp.close()
    dir_name = os.getcwd()
    suffix = '.txt'
    dst_path = os.path.join(dir_name, "temp" + suffix)
    shutil.copyfile(src_path, dst_path)
    name = ""
    url = ""
    with open('temp.txt', 'r') as f:
        name = fn('"name":', f)
        f.seek(0)
        url = fn('"url":', f)
    tn = name[:len(name)-2]
    tu = url[:len(url)-2]
    print('Name = %s' % tn)
    print('Site = %s' % tu)

    word = "click"
    count = 0
    with open("temp.txt", 'r') as f:
        for line in f:
            words = line.split("\"")
            for i in words:
                if (i == word):
                    count = count+1
    print("\n")
    # print('*' * 20)
    print("Number of ",  word+"s", " executed by user ", ":", count)
    os.remove("temp.txt")
    print("\n")

else:
    print('The specified file does NOT exist')
