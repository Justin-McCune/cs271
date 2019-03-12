# Translate .asm file into a fresh created .hack File
# Written in Python for C271, Winter Term at OSU
# Author : Justin Clayton McCune
# Date : 3-7-2019

## To add full functionality :
    # strip anything starting with a paren
    # strip the r after the @
    # concerning 'variables'
        # when we encounter a new variable, search the list
        # if it exists, give it the relavant address
        # if it does not exist store the variable in the list with a ROM location

#Hola mis amigos
#de donde eres?

#   variable declarations
lineList=[]                         #list of lines from the file

#comp bits
    #Destination bit list
destList =    ["D",   "M",   "A",   "MD",  "AM",  "AD",  "AMD"]
binDestList = ["010", "001", "100", "011", "101", "110", "111"]
    #Compute bit list
compList =    ["0",       "1",       "-1",      "D",        "A",       "!D",      "!A",      "-D",      "-A",      "D+1",      "A+1",     "D-1",     "A-1",     "D+A",     "D-A",     "A-D",     "D&A",     "D|A",
                    "M",       "!M",      "-M",      "M-1",     "D+M",     "D-M",     "M-D",     "D&M",     "D|M"]
binCompList = ["0101010", "0111111", "0111010", "0001100",  "0110000", "0001101", "0110001", "0001111", "0110011", "0011111",  "0110111", "0001110", "0110010", "0000010", "0010011", "0000111", "0000000", "0010101",
                    "1110000", "1110001", "1110011", "1110010", "1000010", "1010011", "1000111", "1000000", "1010101" ]
    #jump bits
parmList =    ["D",      "0"]
binParmList = ["001100", "101010"]
conditionList =    ["JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]
binConditionList = ["001", "010", "011", "100", "101", "110", "111"]


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


    #specified ROM address
    if(word[1].isdigit() or word[2].isdigit()):
        if(word[2].isdigit()):
            #shed the R, and move on
            word=word.replace("R", "")
            #shed the @
        newWord = word[1:]
        #convert to binary and strip leading jazz
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
    #no specified ROM address
    else:
        word=word.replace("@","")
        #now we have a 'Variable', it needs to be paired with an address_function
        # we could read through all of the @R commands first to build our variables table
        # then run through the file a second time, this time calling appending_function()
    variables = ["tomatoe", "burger", "burrito", "soup"]



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
    if (word[0]=="/" or word[0]=="\r" or word[0]=="("):
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
