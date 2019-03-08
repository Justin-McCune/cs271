# Translate .asm file into a fresh created .hack File
# Written in Python for C271, Winter Term at OSU
# Author : Justin Clayton McCune
# Date : 3-7-2019


#   variable declarations
lineList=[]                         #list of lines from the file

#comp bits
    #Destination bit list
destList = ["D", "M"]
binDestList = ["010", "001"]
    #Compute bit list
compList = ["M", "D-M", "D"]
binCompList = ["1110000", "1010011", "0001100"]

#jump bits
    #Jump parameter bit list
parmList = ["D", "0"]
binParmList = ["001100", "101010"]
    #Jump condition bit list
conditionList = ["JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]
binConditionList = ["001", "010", "011", "100", "101", "110", "111" ]


#open import file
import sys
importFile = open (sys.argv[1])

#build new file name for export
fileName=sys.argv[1]
a=fileName.split(".")
newFileName=a[0]
newFileName+=".hack"
exportFile = open(newFileName, "a")

def jump_function(word):
    #bit address : 111a cccc ccdd djjj
    #              1110 xxxx xx00 0xxx
    split=word.split(";")
    a=(split[0])
    b=(split[1])
    b=b.replace("\r\n", "")
    parm = parmList.index(a)
    condition = conditionList.index(b)
    bitList = "1110"
    bitList += binParmList[parm]
    bitList += "000"
    bitList += binConditionList[condition]
    appending_function(bitList)

def comp_function(word):
    #filter jump functions
    if(word[1]==";"):
        jump_function(word)
    #comp instructions:
        # 16 bit instruction : 111accccccdddjjj
        # .asm file format   : dest = compute
    else:
        #split the command into dest and comp
        split=word.split("=")
        a=(split[0])
        b=(split[1])
        c=b.replace("\r\n", "")
        #grab the index of the bits from the destList
        dest = destList.index(a)
        #grab the index of the bits from the compList
        comp = compList.index(c)
        #grab the values from the respective lists
        bitList="111"
        bitList+=binCompList[comp]
        bitList+=binDestList[dest]
        bitList+="000"
        appending_function(bitList)

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
    if (word[0]=="/" or word[0]=="\r"):
        del lineList[indx]
        length = len(lineList)
    else:
        indx += 1
#call appropriate functions
length = len(lineList)
indx = 0
while indx < length:
    word = lineList[indx]
    if(word[0]=="@"):
        #call a function to deal will address commands
        address_function(word)
    else:
        #call a function to deal with comp commands
        comp_function(word)
    indx += 1
