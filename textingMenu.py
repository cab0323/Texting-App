"""
Done. This file contains the functions that create the gui.

***might need to add button to set which directory to read.
"""

import tkinter
from tkinter import *
from callNumber import *

box = tkinter.Tk()
box.title("Texting App")
box.geometry('450x450')

#get the size to know where to place text 
box.update_idletasks()
print("Height: ")
print(box.winfo_height())
halfWidth = int(box.winfo_width() / 2)
halfHeight = int(box.winfo_height() / 2)

print("Half Width: ", halfWidth)
print("Half Height: ", halfHeight)

#adding words and buttons
mainFont = 50

#set title
Inputtitle = Label(box, text="Adding New User", font=mainFont)

#first name box
askFName = Label(box, text = "Enter First Name")
firstName = Entry(box, width=20)

#last name
askLName = Label(box, text="Enter Last Name")
lastName = Entry(box, width=20)

#phone number 
askPhone = Label(box, text="Enter Phone Number")
parenthesesLeft = Label(box, text="(", font=1)
parenthesesRight = Label(box, text=")", font=1)
slash = Label(box, text="-", font=1)
areaCode = Entry(box, width=4)
prefix = Entry(box, width=4)
lineNumber = Entry(box, width=4)


#email
# askEmail = Label(box, text="Enter Email")
# userEmail = Entry(box, width=20)

errorMessage = Label(box, text="Make sure boxes with * besides them are not empty")


def getInput():
    #first make sure input is enterd
    key = 0
    if(firstName.get() == ""):
        newText = askFName.cget('text')
        if "*" not in newText:
            newText = newText + "*"
        askFName.config(text=newText)
        key = 1
    if(lastName.get() == ""):
        newText = askLName.cget('text')
        if "*" not in newText:
            newText = newText + "*"
        askLName.config(text=newText)
        key = 1 
    # if(userEmail.get() == ""):
    #     newText = askEmail.cget('text')
    #     if "*" not in newText:
    #         newText = newText + "*"        
    #     askEmail.config(text=newText)
    #     key = 1
    if(areaCode.get() == "") or (prefix.get() == "") or (lineNumber.get() == ""):
        newText = askPhone.cget('text')
        if "*" not in newText:
            newText = newText + "*"        
        askPhone.config(text=newText)
        key = 1
    
    if not key == 1: 
        #pass the info to the bakcend
        completePhone = areaCode.get() + prefix.get() + lineNumber.get()
        #inputUser(firstName.get(), lastName.get(), completePhone)
        person = Person(firstName.get(), lastName.get(), completePhone)
        inputUser(person)

        #clear the input screen and reset it
        firstName.delete(0, 'end')
        lastName.delete(0,'end')

        #delete phone number part by part
        areaCode.delete(0, 'end')
        prefix.delete(0, 'end')
        lineNumber.delete(0, 'end')

        # userEmail.delete(0,'end')
        errorMessage.place_forget()        
        hide_input_screen()
        show_menu()

    else:
        #let user know info missing
        errorMessage.place(x=0 + 20, y= 450 - 50, anchor='w')


#entry button
doneButton = Button(box, text="Done", height=2, width=5, command= getInput)

#menu functions
def show_menu():
    #hide welcome screen
    welcomeButton.place_forget()
    welcomeText.place_forget()

    print("show menu")
    menuTitle.place(x=halfWidth - 4, y=0 + 50)
    putUserIn.place(x=0+30, y=0+100, anchor='nw')
    showDirectoryButton.place(x=0+30, y=halfHeight + 20, anchor='nw')
    sendText.place(x=halfWidth + 40, y= 0+ 100)
    deleteText.place(x=halfWidth + 40, y=halfHeight + 20)

#hide the main menu
def hide_menu():
    menuTitle.place_forget()
    putUserIn.place_forget()
    showDirectoryButton.place_forget()
    sendText.place_forget()
    deleteText.place_forget()

def show_input_screen():
    #hide the menu
    hide_menu()

    #place every part of input menu
    Inputtitle.place(x= halfWidth - 100, y= 0 + 70)
    askFName.place(x= 0 + 25, y=halfHeight - 100, anchor='nw')
    firstName.place(x=0 +27, y=halfHeight-80, anchor='nw')
    askLName.place(x = 0 + 25, y= halfHeight, anchor='nw')
    lastName.place(x=0 + 26, y = halfHeight + 20, anchor='nw')
    askPhone.place(x= halfWidth + 150, y= halfHeight - 100, anchor='ne')

    #phone number separated into each part
    areaCode.place(x=halfWidth + 67, y=halfHeight - 80, anchor='ne')
    parenthesesLeft.place(x=halfWidth + 40, y=halfHeight-85, anchor='ne')
    parenthesesRight.place(x=halfWidth + 80, y=halfHeight - 85, anchor='ne')
    prefix.place(x=halfWidth + 110, y=halfHeight - 80, anchor='ne')
    slash.place(x=halfWidth  + 130, y=halfHeight - 86, anchor='ne')
    lineNumber.place(x=halfWidth + 160, y=halfHeight - 80, anchor='ne')

    #ask for the email of the users
    # askEmail.place(x= halfWidth + 100, y=halfHeight, anchor='ne')
    # userEmail.place(x=halfWidth + 160, y=halfHeight + 20, anchor='ne')


    doneButton.place(x=halfWidth, y=halfHeight + 100, anchor='center')

def hide_input_screen():
    Inputtitle.place_forget()
    askFName.place_forget()
    firstName.place_forget()
    askLName.place_forget()
    lastName.place_forget()
    askPhone.place_forget()

    #hide phone number 
    areaCode.place_forget()
    prefix.place_forget()
    lineNumber.place_forget()
    parenthesesLeft.place_forget()
    parenthesesRight.place_forget()
    slash.place_forget()

    # askEmail.place_forget()
    # userEmail.place_forget()
    doneButton.place_forget()


"""
This function will print the names of the users in the directory. Will give user option to both 
delete or send message to users. Will take in a variable that will tell function to either give the
option to delte or the option to message a person. 
"""
def printUserNamesDirectory(send_or_delete):

    #read the directory, number returned will say weather directory exist and is not empty
    readStatus = readDirectory()

    if(readStatus == 1):
        #the directory does not exist 
        hide_menu()

        showError = Label(box, text="Directory Does Not Exist", font=25)
        showError.place(x=halfWidth, y=halfHeight, anchor='center')

        def deleteError():
            showError.place_forget()
            errorButton.place_forget()
            show_menu()

        errorButton = Button(box, text="OK!", command=deleteError, width=5, height=2)
        errorButton.place(x= halfWidth, y=halfHeight + 100, anchor='center')

    elif readStatus == 2:
            #the directory is empty
            hide_menu()

            showError = Label(box, text="Directory is Empty", font=25)
            showError.place(x=halfWidth, y=halfHeight, anchor='center')

            def deleteError():
                showError.place_forget()
                errorButton.place_forget()
                show_menu()

            errorButton = Button(box, text="Okay!", command=deleteError, width=5, height=3)
            errorButton.place(x=halfWidth, y=halfHeight + 100, anchor='center')

    else:

        #create the frame used to show users in directory and place it
        deleteUserFrame = Frame(box, bg='white', height=300, width=410)
        deleteUserFrame.place(x=20, y=30, anchor='nw') 

        checkList = []

        #function adds checked user to list that will be used to send messages/delete user later
        def addList(p):
            """
            first check if the name is not in list already, as this is easiest way to 
            get around checking and unchecking box
            """
            if p in checkList:
                checkList.remove(p)
            else:
                checkList.append(p)
        

        yLocation = 32
        count = 0
        
        #print the inventory
        for x in readStatus:
            count += 1

            firstName = x.getFName()
            lastName = x.getLName()
            directoryPhone = x.getPhone()

            name = str(count)+ "." + firstName + " " + lastName

            #separate phoneNumber into its 3 parts
            phoneAreaCode = directoryPhone[:3]
            phoneMiddle = directoryPhone[3:6]
            phoneLast = directoryPhone[-4:]

            #format the parts of the phone number to make more readable
            phoneAreaCode = "(" + phoneAreaCode + ")"
            phoneMiddle = "-" + phoneMiddle + "-"

            #put number together to print readibly
            directoryPhone = phoneAreaCode + phoneMiddle + phoneLast

            #put the info together to print
            userCompleteInfo = name + " " + directoryPhone

            #add name of users to the frame
            testFrameLabel = Label(deleteUserFrame, text=userCompleteInfo, font=('Arial', 12), bg='white')
            testFrameLabel.place(x=0, y=0 + (yLocation * count))

            #create dictionary that will hold var of each checkbox, will be used to reset them at end
            intvar_dict = {}
            intvar_dict[count] = IntVar()            

            #print the delete checkbox or the send message checkbox
            if send_or_delete == "delete":
                #add checkbox to delete users
                deleteThisUserCheckbox = Checkbutton(deleteUserFrame, text="Delete", onvalue=x.getFName(), 
                                        variable=intvar_dict[count],command=lambda x = x:
                                        addList(x))
                deleteThisUserCheckbox.place(x=320, y=0 + (yLocation * count))
            elif send_or_delete == "send":
                #each checkbox will stay attached to the x at the time they are created
                sendTextCheckbox = Checkbutton(deleteUserFrame, text="Message", onvalue=x.getFName(), 
                                        variable=intvar_dict[count],command=lambda x = x:
                                        addList(x))
                sendTextCheckbox.place(x=320, y=0 + (yLocation * count))

        #definition to clear frame
        def clearDirectoryFrame(show_or_not_menu):
            deleteUserFrame.place_forget()
            goHomeButton.place_forget()

            if send_or_delete == "send":
                sendMessage.place_forget()
                for currentBox in intvar_dict.values():
                    currentBox.set(0)
            elif send_or_delete == "delete":
                deleteUsersSelected.place_forget()
                for currentBox in intvar_dict.values():
                    currentBox.set(0)
            
            if show_or_not_menu == "show":
                show_menu()

        #delete the messages
        def doneDeletingOrSending(sent_deleted):
            if sent_deleted == "deleted":
                deletingUserLabel.place_forget()
                doneDeletingButton.place_forget()
            elif sent_deleted == "sent":
                sendingMessage.place_forget()
                doneSendingButton.place_forget()
            
            show_menu()
                

        #delete the users selected
        def deleteSelectedUsers():
            clearDirectoryFrame("dont")
            deleteUserFromFile(checkList)
            #delete selected users

            #show the that users are being delted
            global deletingUserLabel
            global doneDeletingButton
            deletingUserLabel = Label(box, text="Deleting Users Selected", font=23)
            deletingUserLabel.place(x=halfWidth, y=halfHeight, anchor='center')
            doneDeletingButton = Button(box, text="Done", fg='red', height=3, width=6,
                                        command=lambda:doneDeletingOrSending("deleted"))
            doneDeletingButton.place(x=halfWidth, y= halfHeight + 50)

        def sendTextDefinition():
            clearDirectoryFrame("dont")
            #deleteUserFromFile(checkList)
            global sendingMessage
            global doneSendingButton
            sendingMessage = Label(box, text="Message Output here!", font=23)
            sendingMessage.place(x=halfWidth, y=halfHeight, anchor='center')
            textOutcome = sendTheText(checkList)
            if textOutcome == 1:
                sendingMessage.config(text="No users selected!")
            elif textOutcome == 2:
                sendingMessage.config(text="Message Not Sent!")
            else:
                sendingMessage.config(text="Message sent!")

            doneSendingButton = Button(box, text="Done", width=6, height=3,
                                       command=lambda:doneDeletingOrSending("sent"))
            doneSendingButton.place(x=halfWidth, y=halfHeight + 50)

        #print button to delete users selected or button to send message to users selected
        if send_or_delete == "send":
            #this button that will send message to users with checkbox beside their name checked 
            sendMessage = Button(box, text="Send", fg='red', height=3, width=6,
                                 command=sendTextDefinition)
            sendMessage.place(x=halfWidth + 30, y=450 - 100)
        elif send_or_delete == "delete":
            #this button that will delete the people checked
            deleteUsersSelected = Button(box, text="Delete", fg='red', height=3, width=6, command=deleteSelectedUsers)
            deleteUsersSelected.place(x=halfWidth + 30, y=450 - 100)
        
        #done printing button will erase screen and go back to main menu
        goHomeButton = Button(box, text="Go Home", fg='red', width= 8, height= 3, 
                              command=lambda:clearDirectoryFrame("show"))
        goHomeButton.place(x=halfWidth - 80, y= 450-100)



def hideMenuCallDirectory(to_delete_send):
        hide_menu()

        if to_delete_send == "delete":
            #call the function to print the names already in directory, with a button to delete each user
            printUserNamesDirectory("delete")
        elif to_delete_send == "send":
            printUserNamesDirectory("send")
        else:
            #just print the directory without deleting or sending
            printUserNamesDirectory("neither")


#welcome text 
welcomeText = Label(box, text="Welcome To App", font=50)
welcomeText.place(x=halfWidth, y=halfHeight, anchor='center')

#button to start
welcomeButton = Button(box, text="Start", fg='red', command=show_menu,height=3, width=10)
welcomeButton.place(x= halfWidth, y=halfHeight + 50, anchor='center')

#menu
menuTitle = Label(box, text="Menu", font=10)

#option 1:get user input
putUserIn = Button(box, text="Input Person", fg='red', width=12, height=3, font=5, command=show_input_screen)

#option 2: read directory
showDirectoryButton = Button(box, text="Read Directory", fg='red', width= 12, height=3, font=5, 
                             command=lambda:hideMenuCallDirectory("neither"))

#option 3:send text
sendText = Button(box, text="Send Text", fg='red', width=12, height= 3, font=5, 
                  command=lambda:hideMenuCallDirectory("send"))

#option 4:delete user
deleteText = Button(box, text="Delete User", fg='red', width=12, height=3, font=5, 
                    command=lambda:hideMenuCallDirectory("delete"))


box.mainloop()
