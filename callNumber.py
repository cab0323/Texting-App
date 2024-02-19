"""
Done. This file contains the functions that directly interact with the file.
Write and read from the file.
"""

import smtplib
import os
from email.message import EmailMessage #import used to send the text message


directory = 'directory2.txt'

#the array of carrier emails
carrier_emails = []
carrier_emails.append('@text.att.net')
carrier_emails.append('@vtext.com')
carrier_emails.append('@tmomail.net')


#class used to describe a person. 
class Person:
    #class method
    def __init__(self, firstName, lastName, phoneNumber):
        self.fName = firstName
        self.lName = lastName
        self.phone = phoneNumber
        #self.email = email

    #override function to compare two objects of Person class
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        
        #return true if first and last name are equal
        if self.fName == other.fName and self.lName == other.lName:
            return True

    def printName(self):
        print("Name is: " + self.fName)

    def getFName(self):
        return self.fName

    def getLName(self):
        return self.lName

    def getPhone(self):
        return self.phone
    

#put Persons info into the file
def inputUser(person):
    with open(directory, 'a') as file:
        file.write(person.getFName() + " ")
        file.write(person.getLName() + " ")
        file.write(person.getPhone() + "\n")

#function that sends the text to selected users/user
"""
left commented out since i dont want to send a message to soemone everytime i 
runt the code to test it
"""
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

        #try sending to each carrier email until it gets the right one
        while True:
            #set the count to keep track of which carrier to send to 
            i = 0
            recipientEmail = person.getPhone() + carrier_emails[i]
            print("email to send to: " + recipientEmail)

            try:
                msg = EmailMessage()
                msg.set_content('Dear ' + recipient + ', This is a test message.')

                msg['Subject'] = 'Testing'
                msg['From'] = 'cabrerachris.9873@yahoo.com'
                msg['To'] =   recipientEmail

                # s = smtplib.SMTP("smtp.mail.yahoo.com", 587)
                # #login in to server
                # s.starttls()
                # s.login('cabrerachris.9873@yahoo.com', 'blfvjxiknjacgbns')

                # #finally send message
                # print("Sending Message")
                # s.send_message(msg)
                # print("Message SENT")
                # s.quit()
                # print("Messages sent to: " + recipient)
                # break

            except smtplib.SMPTPException:
                print("Message Not sent")
                #message not sent, try again only if it's not the last email carrier 
                if i >= len(carrier_emails):
                    print("None of the carriers worked")
                    textFlag = 2
                    return textFlag
                    break
                #else try again
                i += 1
            

#function to read the directory
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

#function that deletes the users selected
def deleteUserFromFile(deleteList):
    #create list of users that wont be deleted, and will be readded
    namesToReAdd = []

    #open file and read each line first
    with open(directory, 'r') as readFile:
        #read the directory line by line
        for line in readFile:
            #split the line into its parts[firstName, lastName, phoneNumber]
            userInfo = line.split()

            #create a person object from the info read from directory
            currentPersonInDirectory = Person(userInfo[0],userInfo[1], userInfo[2])

            #keep track of weather the current line read from directory will be readded to the file
            reAddName = True

            #iterate through list to see if user in list
            for personInList in deleteList:
                if currentPersonInDirectory == personInList:
                    reAddName = False
            
            #if name is not in deleteList readd it
            if reAddName:    
                namesToReAdd.append(currentPersonInDirectory)
    
    with open(directory, 'w') as writeFile:
        #add the names back to the file
        for p in namesToReAdd:
            writeFile.write(p.getFName() + " ")
            writeFile.write(p.getLName() + " ")
            writeFile.write(p.getPhone() + "\n")

