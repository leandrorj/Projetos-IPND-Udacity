import os

def rename_file():
    file_list = os.listdir(r"C:\un4")
    saved_path = os.getcwd()
    print("Diretorio" +saved_path)
    os.chdir(r"C:\un4")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_file()
