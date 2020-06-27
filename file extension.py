#Write a Python program to accept a filename from the user and print the extension of that.
name=input("Input the file name")
ext= name.split(".")
print("file extansion is:" + repr(ext[1]))





