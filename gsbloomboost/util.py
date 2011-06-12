import os

""" General purpose utilities"""

def if_file_exists(file_name):
        """ Pass full file path to do this check"""
        return os.path.exists(file_name)

#if __name__ == "__main__":
#    print Util.ifFileExists("/Users/vivekris/GS/code/gsbloomboost/gsbloomboost/main.py")

