# CS 374 -1 Database Management
# Atticus, Emma, Bo, Shane
# 12/15/22
# Resources: 
# Embedded SQL Slides from Pete, 
# https://www.geeksforgeeks.org/python-store-function-as-dictionary-value/
#

#database stuff
import pymysql 
db = pymysql.connect(host = 'database-final.cazc7ungu94n.us-west-2.rds.amazonaws.com', user = 'admin', password= 'Sheba123!', database= 'final' )
crsr = db.cursor()

#global variables that make things 1304304 times easier for us
pastUser = -1
userID = -1
userFirstName = ''
userLastName = ''
userBudget = ''
userState = ''
userIndustry = ''
userBtype = ''


#this function helps to return the information on the business type that the user wants to know about
def getBTypes(bType):
    #create btypes query
    query = 'Select b.* From BType as b Where b.name=\"' + bType +'\"'
    res = crsr.execute(query)
    returnString = ''
    isName = True
    #make the return string look nice
    for i in crsr:
        for j in i:
            if isName:
               returnString = returnString + j + ": " 
               isName = False
            else:
                returnString = returnString + j + " "
    returnString = returnString.replace('+', ', ')

    #store the column values
    returnStringColumns = []
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and actual data
    return returnStringColumns, returnString

#this function finds the max id from the users, then increments it by one and creates a new user with that id
def getNewUsersID():
    #return users
    query = 'Select Max(ID) From Users'
    res = crsr.execute(query)
    for i in crsr:
        return int(i[0]) + 1

#this function retrieves the current user from the database
def getCurrentUser(ID):
    invalidData = True
    while invalidData:
        query = 'Select u.* From Users as u Where u.ID = ' + ID
        res = crsr.execute(query)
        if res == 0:
            ID = input("Select valid id please")
        else:
            for i in crsr:
                invalidData = False
                return i

#this function gets the current market description of the industry that they are in
def getMarketDescriptions(userIndustry):
    query = 'Select i.* from Industry as i where name = \"' + userIndustry + '\"' 
    res = crsr.execute(query)
    returnString = ''
    isName = True
    #make the return string look nice
    for i in crsr:
        for j in i:
            if isName:
               returnString = returnString + j + ": " 
               isName = False
            else:
                returnString = returnString + j + " "
    returnStringColumns = []
    #store column data
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and data
    return returnStringColumns, returnString
    
#this function returns all of the patent resources
def getPatentRes():
    query = 'Select p.* From PatentResources as p where p.industry = \"any\" or p.industry =\"' + userIndustry + '\"'
    res = crsr.execute(query)
    returnList = []
    for i in crsr:
        returnList.append(i)
    returnStringColumns = []
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and data
    return returnStringColumns, returnList

#this function returns all of the legal resources that are specific to the user
def getLegalRes():
    query = 'Select l.* From LegalResources as l where (l.state = "FED" or l.state =\"' + userState + '\") and (l.budget =\"' + userBudget + '\" or l.budget = "Any")'
    res = crsr.execute(query)
    returnList = []
    for i in crsr:
        returnList.append(i)
    returnStringColumns = []
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and data
    return returnStringColumns, returnList

    

#this function returns all of banking resources that are relevant to the user
def getBankingRes():
    query = 'Select b.* From BankingResources as b where (b.state = "FED" or b.state =\"' + userState + '\") and (b.bType =\"' + userBtype + '\" or b.bType = "Any")'
    res = crsr.execute(query)
    returnList = []
    for i in crsr:
        returnList.append(i)
    returnStringColumns = []
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and data
    return returnStringColumns, returnList

def getTaxRes():
    query = 'Select t.* from TaxResources as t where (t.state = "FED" or t.state =\"' + userState + '\") and (t.bType =\"' + userBtype + '\" or t.bType = "Any")'
    res = crsr.execute(query)
    returnList = []
    for i in crsr:
        returnList.append(i)
    returnStringColumns = []
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and data
    return returnStringColumns, returnList

#this function returns relevant certifications for the user
def getCertifications():
    query = 'Select c.* From Certifications as c Order By priority'
    res = crsr.execute(query)
    returnList = []
    for i in crsr:
        returnList.append(i)
    returnStringColumns = []
    for i in crsr.description:
        returnStringColumns.append(i[0])
    #return columns and data
    return returnStringColumns, returnList


#this is the start of the driver code, checks to see if the user has been there before
pastUser = input("Hello! Have you used this application before? If so, press 1. If not, press 2 --->")
#if the user has been there before, they need to write their id number to sign in
if pastUser == "1":
    userID = input("Please enter your id number: ")
    i = getCurrentUser(userID)
    #now the global info about the user will be updated
    userID = i[0]
    userFirstName = i[1]
    userLastName = i[2]
    userBudget = i[3]
    userState = i[4]
    userIndustry = i[5]
    userBtype = i[6]
    
#if someone hasn't used the program before, then they can create a new profile
else:
    print("Welcome new user! Please input your relevant information: ")

    #basic input for first name, last name, and budget size
    userFirstName = input("Please enter your first name ")
    userLastName = input("Pleaser enter your last name ")
    userBudget = int(input("Is your budget 1: Small (0-10k)   2: Medium (10k-20k)   3: Large (20k+)  (Select 1, 2, or 3) --->"))



    #allocate userbudget based on the user's choice
    if userBudget == 1:
        userBudget = "Small"
    elif userBudget == 2:
        userBudget = "Medium"
    else:
        userBudget = "Large"
    
    #same process as userbudget but for the state that someone is in. Right now, we only have washington data
    userState = int(input("Select the state you are in:   1. WA    2. OR     3. CA  (Select 1, 2, or 3) --->"))
    if userState == 1:
        userState = "WA"
    elif userState == 2:
        userState = "OR"
    else:
        userState = "CA"


    #same process here as well
    userIndustry = int(input("Please enter the industry you are in:     1. Agriculture      2. Healthcare       3. Restaurant       4. Retail   --->"))
    if userIndustry == 1:
        userIndustry = "Agriculture"
    elif userIndustry == 2:
        userIndustry = "Healthcare"
    elif userIndustry == 3:
        userIndustry = "Restaurant"
    else:
        userIndustry = "Retail"

    #ask user if they want market descriptions shown
    getIndustryInformation = input("Would you like a market description of the industry you chose? (Y/N) --->")
    
    #show usere the market description for their industry
    if getIndustryInformation == 'Y' or getIndustryInformation == 'y':
        response = getMarketDescriptions(userIndustry)[1]
        print(response)
        print()
        

    #ask user if they was to learn about llc's, s corps, etc
    giveUserBtypeInfo = input("Would you like to learn about the kinds of businesses there are? (Y/N) --->")
    userChoice = -1
    #user can keep getting info until they don't want it anymore
    while giveUserBtypeInfo == 'Y' or giveUserBtypeInfo == 'y':
        businessTypes = ["LLC", "C Corp", "S Corp", "DBA"]
        userChoice = int(input("Please enter the number of the business type that you want to learn about      1. LLC      2. C Corp       3. S Corp       4. DBA  --->"))
        #check for bad input
        if userChoice > 4 or userChoice < 1:
            print("Please enter valid input")
        else:
            #see if we want to be in the loop still
            print(getBTypes(businessTypes[userChoice-1])[1])
            giveUserBtypeInfo = input("Do you want to learn about another business type? Y/N --->")
        
    #have the user select their business type
    userBtype = int(input("Please enter the business type that you own      1. LLC      2. C Corp       3. S Corp       4. DBA  --->"))
    if userBtype == 1:
        userBtype = "LLC"
    elif userBtype == 2:
        userBtype = "C Corp"
    elif userBtype == 3:
        userBtype = "S Corp"
    else:
        userBtype = "DBA"

    #get a new id for the user
    userID = getNewUsersID()

    #make a new user query
    query = 'INSERT INTO final.Users (ID, fName, lName, budget, state, industry, bType) Values( \'' + str(userID) + '\',\'' + userFirstName + '\',\'' + userLastName + '\',\'' + userBudget + '\',\''+ userState + '\',\'' + userIndustry + '\',\'' + userBtype + '\');'

    #execute the query
    res = crsr.execute(query)
    db.commit()

print()
print()

#customize welcome message
if pastUser == '1':
    print("Welcome back " + userFirstName + '! ', end=' ')
else:
    print("Welcome " + userFirstName + '! ', end=' ')

#See what the user wants from the program
userInput = 0
userNeeds = []
print("Select everything you need from us to send to you please! Select you options and then type in \"DONE\" when you are complete :) ")
print()
print("1. Necessary Certifications      2. Legal Resources      3. Patent Resources     4. Tax Resources        5. Banking Resources      ")

#get what the user wants, don't let there be copies of data
while userInput != "DONE":
    userInput = int(input("Select resource number --->"))
    if userInput < 1 or userInput > 5:
        print("Please give valid input")
    #checks for redundant data
    elif userInput in userNeeds:
        print("You already asked for that! Please choose another option")
    else:
        userNeeds.append(userInput)
        #if user has chosen every resource, then exit the loop
        if len(userNeeds) == 5:
            print("Great, you chose every resource!")
            userInput = "DONE"
        else:
            userInput = input("Would you like to continue? If so, press enter. If not, write \"DONE\" --->")
#sort the data because options are given based on priority of importance
userNeeds.sort()

#From https://www.geeksforgeeks.org/python-store-function-as-dictionary-value/
mapFunctions ={1 : getCertifications, 2 : getLegalRes, 3 : getPatentRes, 4: getTaxRes, 5 : getBankingRes}

#open the file and add some personal stuff to it
fileForUser = open("BusinessPlan.txt", "w")
messageToUser = "Here is your personalized business resource plan based on your state, budget, business type, and industry! \n"
fileForUser.write(messageToUser)
userData = "User Data ---> User ID: " + str(userID) + ", User Name: " + userFirstName + " " + userLastName + ", User Budget: " + userBudget + "\n                User State: " + userState + ", User Business Type: " + userBtype + ", User Industry: " + userIndustry 
fileForUser.write(userData + "\n\n")


#add all of the data into the file based on what the user chose 
for i in userNeeds:
    if i == 1:
        fileForUser.write("Necessary Certifications: \nMake sure to get your certifications in this order! \n\n")
    elif i == 2:
        fileForUser.write("Legal Resources: \n\n")
    elif i == 3:
        fileForUser.write("Patent Resources: \n\n")
    elif i == 4:
        fileForUser.write("Tax Resources: \n\n")
    else:
        fileForUser.write("Banking Resources: \n\n")
    counter = 0
    #calls correct function and writes all the columns to the file
    for j in mapFunctions[i]()[0]:
            fileForUser.write(str(j) + " ")
            counter += 1
    fileForUser.write('\n\n')
    secondCounter = 1
    #writes all the data from the file that is called from the correct function based on the map
    for j in mapFunctions[i]()[1]:
        for k in j:
            if secondCounter != counter:
                fileForUser.write(str(k) + ", ")
            else:
                fileForUser.write(str(k) + " ")
            secondCounter += 1
        secondCounter = 1
        fileForUser.write('\n')
    fileForUser.write("\n\n")

print()

print("Check the file directory for your own personalized business resource!")


