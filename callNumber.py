

import smtplib
import os
#imports for UI

def clicked():
    print("Test!!")

from email.message import EmailMessage


# #--- program works, get UI above
# #-- delete function not done yet

directory = 'directory2.txt'


#need to add getNumber and get email to person class
#class to send back to gui
class Person:
    #class method
    def __init__(self, firstName, lastName, phoneNumber):
        self.fName = firstName
        self.lName = lastName
        self.phone = phoneNumber
        #self.email = email

    def printName(self):
        print("Name is: " + self.fName)

    def getFName(self):
        return self.fName

    def getLName(self):
        return self.lName

    def getPhone(self):
        return self.phone
    

#defining my fucntions to call after we get user input
def inputUser(person):
    with open(directory, 'a') as file:
        file.write(person.getFName() + " ")
        file.write(person.getLName() + " ")
        file.write(person.getPhone() + "\n")

def sendTheText(listNames):

    """
    0 returned if the message was sent correctly
    1 returned if no users selected
    2 retuned if text wasnt sent, encountered problem
    """
    textFlag = 0

    #check if file exist first
    if not listNames:
        print("list is empty")
        textFlag = 1
        return textFlag

    for person in listNames:
        #print name and email
        recipient = person.getFName()
        recipientEmail = person.getPhone() + '@text.att.net'
        print("Recipient: " + recipient, end=" ")
        print("Recipient Address: " + recipientEmail + "\n")
        # userConfirm = input("Send message? (Y/N): ")

        try:
            # msg = EmailMessage()
            # msg.set_content('Dear ' + recipient + ', This is a test message.')


            # msg['Subject'] = 'Testing'
            # msg['From'] = 'cabrerachris.9873@yahoo.com'
            # msg['To'] =   recipientEmail

            # s = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            # #login in to server
            # s.starttls()
            # s.login('cabrerachris.9873@yahoo.com', 'blfvjxiknjacgbns')

            # #finally send message
            # print("Sending Message")
            # s.send_message(msg)
            # print("Message SENT")
            # s.quit()
            print("Messages sent to: " + recipient)
        except smtplib.SMPTPException:
            print("Message Not sent")
            textFlag = 2
            return textFlag


def readDirectory():
    #will be returned if something is wrong
    errorFlag = 0 #nothing is wrong
    
    #check if file exist first
    if not os.path.isfile(directory):
        print("DIRECTORY DOES NOT EXIST!")
        errorFlag = 1
        return errorFlag
        #exit()

    #open the file for reading only 
    with open(directory, 'r') as readFile:
        #first check that file is not empty
        if os.stat(directory).st_size == 0:
            print("DIRECTORY IS EMTPY!!")
            errorFlag = 2
            return errorFlag
            #exit()

        #declare list that will hold people info and be returned
        people = []

        #read file line by line and print results
        while True:
            currentLine = readFile.readline()
            words = currentLine.split()

            #check if no more line read, means done
            if not currentLine:
                print("NO MORE LINE")
                break


            print("words: ", words)
            print("Words[0]: " + words[0])
            print("Words[1]: " + words[1])
            person = Person(words[0], words[1], words[2])
            people.append(person)
            currentLine = currentLine.rstrip()
            print("\n")


    #test class
    # p = Person("Christian", "Cabrera", "8645063150", "0913chrsi@gmail.com")
    # p.printName()

    directoryList = []
    #directoryList.append(p)
    #return directoryList

    return people




def deleteUserFromFile(person):
    #get the name of user
    print("What user do you want to delete?")
    deleteFName = person.getFName()
    deleteLName = person.getLName()

    #test
    print("FName: " + deleteFName)
    print("LName: " + deleteLName)

    #create list of users that wont be deleted
    namesToReAdd = []

    #open file and read each line first
    with open(directory, 'r') as readFile:
        for line in readFile:
            userInfo = line.split()
            print("First Names: " + userInfo[0])
            #find user to delete
            if not deleteFName == userInfo[0] and not deleteLName == userInfo[1]:
                #add all names except this one
                currentPerson = Person(userInfo[0], userInfo[1], userInfo[2])
                namesToReAdd.append(currentPerson)
    
    with open(directory, 'w') as writeFile:
        print("Names will be readded: ")
        #add the names back to the file
        for p in namesToReAdd:
            writeFile.write(p.getFName() + " ")
            writeFile.write(p.getLName() + " ")
            writeFile.write(p.getPhone() + "\n")


# while True:
#     #first get user input on what they want to do
#     print("\n")
#     print("Welcome to Call Number")
#     print("Please read the following menu")
#     print("1. Add person to directory")
#     print("2. Send text")
#     print("3. Read Directory")
#     print("4. Delete User")
#     print("5. Exit Program")
#     userSelection = input("Make Selection: ")

#     #check if user wants to quit program 
#     if userSelection == '5':
#         print("Thanks for using!")
#         exit()
    
#     if not userSelection.isdigit():
#         print("ENTER ONLY NUMERICAL INPUT")
#         continue

#     #get directory specification
#     directory = input("Please specify which directory as well: ")
    
#     #modify input to desired type
#     userSelection = int(userSelection)
#     directory = directory + '.txt'

#     #interpretate users input
#     if userSelection == 1:
#         #user wants to add new user
#         inputUser()
#     elif userSelection == 2:
#         #user wants to send texts
#         sendText()
#     elif userSelection == 3:
#         #user wants to read directory
#         readDirectory()
#     elif userSelection == 4:
#         #user wants to delete user
#         deleteUser()
#     else:
#         print("Please make valid selection")



