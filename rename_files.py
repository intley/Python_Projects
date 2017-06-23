import os

#Program that renamed a bunch of my files in a folder and removed any numbers present in them.
#helps reveal my secret message.
def rename_files():
    #1 : Get file names from the folder

    file_list = os.listdir(r"/Users/Rahul/Documents/Udacity Full_Stack_Nanodegree/prank")
    print(file_list)

    saved_path = os.getcwd()
    print("Current working directory is: " + saved_path)

    os.chdir(r"/Users/Rahul/Documents/Udacity Full_Stack_Nanodegree/prank")
    print("New working directory is: " +os.getcwd())
    
    #2 : For each file, rename filename
    for file_name in file_list:
            print("Old name: " +file_name)
            os.rename(file_name, file_name.translate(None, "0123456789"))
            print("New name: " + file_name.translate(None, "0123456789"))
            print("\n")
    os.chdir(saved_path)
        

rename_files()
