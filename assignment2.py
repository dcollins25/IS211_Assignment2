import argparse
import urllib.request
import logging
from datetime import datetime
import os

# Check to see if these files below exist, remove them if they do. To be used later ...
if os.path.exists("IS211-ext-file.txt"):
    os.remove("IS211-ext-file.txt")
if os.path.exists("errors.log"):
    os.remove("errors.log")

LOG_FILENAME = 'errors.log'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

parser = argparse.ArgumentParser()
parser.add_argument("URL")
link = parser.parse_args()
#print(link.URL)
strurl = (link.URL)

def downloadData(url):
    try:
        req = urllib.request.urlopen(url)
        decoded = str(req.read().decode('utf-8'))
    except Exception as Argument:
        assignment2 = open(LOG_FILENAME, "a")
        assignment2.write(str(Argument))
        assignment2.close()
        print('\n*** ' + 'An ERROR occurred. Please see \"errors.log\" for more information ***')
        exit()
    return decoded

#content = downloadData('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
csvData = downloadData(strurl)

def processData(file_content):
    myList = file_content.split('\n')
    userdict = {}
    counter = 0
    newDate = ''
    for line in myList:
        counter +=1
        userTuple = line.split(',')
        if len(userTuple) == 3:
            number, person, date = (userTuple)
# PUT LOGGER BELOW
            try:
                newDate = datetime.strptime(date, '%d/%m/%Y')
                #print(type(newDate))
                #print(number, person, newDate)
                newTuple = (number, person, newDate)

            except:
                pass

        userdict = {
            (counter): ((person), (newDate))
                    }
        #print(userdict)
# I COULD NOT GET THE DATA INTO ONE BIG DICTIONARY. IT CREATED 102 INDIVIDUAL DICTIONARIES, SO I DUMPED THE DATA INTO A FILE.
# WHEN THE USER INPUTS THE ID TO SEARCH, I SEARCH THROUGH THE FILE "IS211-ext-file.txt" AND PRESENT THE DATA RETRIEVED FROM THAT.
        userstr = str(userdict)
        outF = open("IS211-ext-file.txt", "a")
        outF.write(userstr)
        outF.write("\n")
        outF.close()

noUser = 0

processData(csvData)

#def displayPerson(id, personData):
#    pass
#
# TAKE STANDARD IN FROM USER AND ASK FOR AN ID
#	- if ID <= 0, end the program
#	- if ID is in file, display the user and date
#	- if ID is not in file, print 'No user # found with that ID'

inputID = input("Please enter the ID of the user you need information on: ") 

integerID = int(inputID)

if integerID <= 0:
    print("Goodbye!")
    exit()

if integerID == 1:
    print("Line 1 is simply a Header. Please choose another value.")
    exit()

searchChars = "{" + inputID + ": "
#print("SEARCHING FOR: " + searchChars)

searchfile = open("IS211-ext-file.txt", "r")
for line in searchfile:
    if searchChars in line: 
        #print(line)
        splitOne = line.split('datetime.datetime(')
        splitOneStr = str(splitOne)
        splitTwo = splitOneStr.split(',')
        splitTwoStr = str(splitTwo[0] + splitTwo[2] + splitTwo[3] + splitTwo[4])
        #print(splitTwoStr)
# SAMPLE DATA: ["{91: ('Sonia Pullman' '1999 9 14
        splitThree = splitTwoStr.split(': (')
        splitThreeStr = str(splitThree[1])
        #print(splitThreeStr)
# SAMPLE DATA: 'Sonia Pullman' '1999 9 14
        splitFour = splitThreeStr.split()
        #print(splitFour)
# SAMPLE DATA: ["'Sonia", "Pullman'", "'1999", '9', '14']

        if len(splitFour[3]) == 1:
            paddedIndexThree = "0" + splitFour[3]
            newIndexThree = paddedIndexThree
        else:
            newIndexThree = splitFour[3]

        if len(splitFour[4]) == 1:
            paddedIndexFour = "0" + splitFour[4]
            newIndexFour = paddedIndexFour
        else:
            newIndexFour = splitFour[4]

        print('\n' + 'Person with # ' + (inputID) + ' is ' + (splitFour[0]) + ' ' + (splitFour[1]) + ' with a birthday of ' + (splitFour[2]) + ' ' + (newIndexThree) + ' ' + (newIndexFour))
        exit()

    else:
        tempF = open(LOG_FILENAME, "a")
        tempF.write('No user # found with that ID')
        tempF.write("\n")
        tempF.close()
        noUser = 1

if noUser == 1:
    print('\n*** ' + 'An ERROR occurred searching for this user ID #. Please see \"errors.log\" for more information ***')

searchfile.close()
