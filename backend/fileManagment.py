import glob
import os

def get_user_files():
    print(os.getcwd())
    return glob.glob(os.getcwd() + "/UserFiles/*.txt")