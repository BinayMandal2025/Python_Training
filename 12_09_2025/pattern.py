import glob
import re

#Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
#Write a script to:
#- Find all .txt files in a folder.
#- Check if any file contains the word "Python".
#- Print the file name if the word is found
print("***********ASSIGNMENT1*****************")
txtfiles = glob.glob("C://RDT//Python//Data Types//Pattern//*.txt")
print(txtfiles)

for txtitem in txtfiles: 
    item1 = re.search(r"Python", txtitem)

if item1:
    print("Python text found, file name:", txtitem)

print("***********ASSIGNMENT2*****************")
#Assignment 2: Match File Names Using re.match
#List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
fileName = glob.glob("C://RDT//Python//Data Types//Pattern//*.*")
#print(fileName)

for items in fileName:
    #print(items)
    newfile = re.sub(r"C://RDT//Python//Data Types//Pattern\\", "", items)
    #print(newfile)
    match1 = re.match(r"^data_.*\.csv$", newfile)
    if match1:
     print("Found CSv File:", newfile)


print("***********ASSIGNMENT3*****************")
#Assignment 3: Validate Phone Numbers with re.match
#Given a list of phone numbers, print only the ones that match this format:
#(123) 456-7890

phone  = "(123) 456-7890, (123) 456-7891, (123) 456-7892, (123) 456-7893"
match = re.match(r"\(123\) 456-7890", phone)

if match:
    print("Phone number found:", match.group())
