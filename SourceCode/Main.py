import os
import pathlib
import sys
import ctypes

def Main():
    pathL = pathlib.Path("C:\\Program Files\\Xigncode3Bypass\\XIGNCODE3_Bypass.pfx")
    if pathL.is_file() is True:
        xigncode3path = os.path.abspath("C:\\Program Files\\Xigncode3Bypass\\XIGNCODE3_Bypass.pfx")
        file_exec = input("Please Write Game Process with XIGNCODE3 AntiCheat: ")
        os.system("signtool sign /f {} /p {}.exe".format(xigncode3path, file_exec))
        print("This Process is now signed successfully... Or not...")
    else:
        exit(10056)
    exit(312)

if __name__ == "__main__":
    Main()