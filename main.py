'''
Replace specified content in a specified file-type, within every subfolder of a provided parent directory 

Zaahier Adams
https://github.com/ZaahierAdams
07 November 2021
'''

from os import walk as os_walk
from os import path as os_path

def inputs():
    print("Warning: All user inputs are case-sensitive!\n")
    source      = input('\n(1) Parent/source Directory: ')
    file_name   = input('\n(2) File name (part-of or full): ') 
    file_ext    = input('\n(3) File extension (eg. json, txt, etc...): ') 
    target      = input('\n(4) Target string: ')
    replace     = input('\n(5) Replacement string: ')
    return source, file_name, file_ext, target, replace

def test_folder(type, item):
    print(f"\n- Scanning {type}: {item}")

def occur_print(file, occur):
    print(f'\n- {occur} replacement(s) made in {file}')

def margin():
    return '-'*30

def output(searched_folders, searched_files, occur_total):
    print("\n"+margin())
    print(f"\n- Folders searched:\t{searched_folders}")
    print(f"- Files searched:\t{searched_files}")
    print(f"- Total replacements:\t{occur_total}\n")
    print(margin())

def hang():
    while True:
        restart = input("restart (y/n)?")
        restart.lower()
        if restart == "y":
            break #oops
        elif restart == "n":
            break
        else:
            pass
            
def main():    
    source, file_name, file_ext, target, replace = inputs()

    searched_folders = 0
    searched_files = 0
    occur_total = 0

    print(margin())
    for root, dirs, files in os_walk((os_path.normpath(source)), topdown=False):
        test_folder("folder",root.split('\\')[-1])
        searched_folders+=1
        for file in files:
            if (file_name in file) and (file.endswith(file_ext)):
                test_folder("file", file)
                searched_files+=1
                dir = root + '\\' + file
                with open(dir, 'r+') as file_opened:
                    content = file_opened.read()
                    if target in content:
                        occur = content.count(target)
                        occur_total+=occur
                        file_opened.seek(0)
                        filedata = content.replace(target, replace)
                        file_opened.write(filedata)
                        file_opened.truncate()
                        occur_print(file, occur)
                    else:
                        occur_print(file, 0)
            else:
                pass
    output(searched_folders, searched_files, occur_total)
    hang()
main()

