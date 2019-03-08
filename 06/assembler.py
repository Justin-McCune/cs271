# Translate .asm file into a fresh created .hack File
# Written in Python for C271, Winter Term at OSU
# Author : Justin Clayton McCune
# Date : 3-7-2019


#   variable declarations
lineList=[]                         #list of lines from the file


#open import file
import sys
importFile = open (sys.argv[1])

#build new file name for export
fileName=sys.argv[1]
a=fileName.split(".")
newFileName=a[0]
newFileName+=".hack"
exportFile = open(newFileName, "a")



# functions to assemble binary code
def address_function(word):
    #establish a new binary command for each line passed
    binary = ""
    bitList =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #process the line, modify appropriate bits
        #convert to binary and strip leading jazz
    newWord = word[1:]
    binNum = bin(int(newWord))
    binNum = binNum[2:]
        #put binary number into list for easier manipulation
    binList=[]
    for x in binNum:
        binList.append(x)
        #reverse binList, merge into bitList, reverse again
    binList.reverse()
    indx = 0
    while indx < len(binList):
        bitList[indx]=binList[indx]
        indx+=1
    bitList.reverse()
        #concatonate the bitList and send to apppending_function
    for bit in bitList:
        binary += str(bit)
    appending_function(binary)

def d_function(word):
    if(word[2]=="M" and len(word)==5):
        appending_function('1111110000010000')

    print(len(word))
def m_function(word):
    print(" ")
def jump_function(word):
    print(" ")

#function to push binary code into new file
def appending_function(binary):
    exportFile.write(binary + "\n")


#put every file line into lineList
for x in importFile:
    lineList.append(x)

#remove comments / fluff from lineList
length = len(lineList)
indx = 0
while indx < length:
    word = lineList[indx]
    if (word[0]=="/"):
        del lineList[indx]
        length = len(lineList)
    else:
        indx += 1

#look
length = len(lineList)
indx = 0
while indx < length:
    word = lineList[indx]
    if(word[0]=="@"):
        #call a function to deal will a-address commands
        address_function(word)
    elif(word[0]=="D" and word[1]=="="):
        #call a function to deal with d=address commands
        d_function(word)
    elif(word[0]=="M" and word[1]=="="):
        #call function to deal with m=address commands
        m_function(word)
    elif(word[1]==";"):
        #call a function to deal with jump commands
        jump_function(word)
    indx += 1
