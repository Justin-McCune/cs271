# Translate .asm file into a fresh created .hack File
# Written in Python for C271, Winter Term at OSU
# Author : Justin Clayton McCune
# Date : 3-7-2019


#   variable declarations
lineList=[]                         #list of lines from the file
                            # iteration variable

#open file
f = open ("max/MaxL.asm")


#function example
def my_function():
    print "Hello from a function"


#put every file line into lineList
for x in f:
    lineList.append(x) #add items to a list
    #my_function()

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
#print current list of commands
for x in lineList:
    print x
print(len(lineList))

#look
length = len(lineList)
indx = 0
while indx < length:
    word = lineList[indx]
    if(word[0]=="@"):
        print("@")
        #call a function to deal will a-address commands
    indx += 1
