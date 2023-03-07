#include <iostream>
#include <fstream>
#include <string>
#include <sstream>


using namespace std;

int main(){
    
    int userSelection;
    cout << "Welcome to TextMachine" << endl;
    cout << "Check the following Menu:" << endl;
    cout << "1. Enter Names into directory" << endl;
    cout << "2. Read Names from directory" << endl;
    cout << "3. Send Emails" << endl;
    cout << "Make a selection: ";
    cin >> userSelection;

    if(userSelection == 1){
        cout << "You chose to enter new names to directory" << endl;
        cout << endl;

        /*add numbers and names to a directory using java as the front end
            creating a quick app for a phone. Then just read from it from 
            c++ */
        ofstream testFile;
        testFile.open("directory.txt", fstream::app);
        //FName, LName, Phone Number
        string firstName;
        string lastName;
        string phoneNumber;
        string email;

        //getting the new person info
        cout << "Enter First Name of new person: ";
        cin >> firstName;
        cout << "Enter Last Name of new person: ";
        cin >> lastName;
        cout << "Enter PhoneNumber of new Person" << endl;
        cout << "Enter with no spaces: ";
        cin >> phoneNumber;
        cout << "Enter your email: ";
        cin >> email;

        //putting person info into the file
        testFile << firstName << " "<< lastName << " " 
        << phoneNumber << " " << email << endl;
        testFile.close();    
    }
    else if(userSelection == 2){
        cout << "You chose to read names from directory:" << endl;
        cout << endl;

        //open file for reading
        ifstream readFile;
        readFile.open("directory.txt");
        if(readFile.fail()){
            cout << "FILE DOES NOT EXIST OR PROBLEM OPENING" << endl;
            exit(0);
        }

        //reading from file
        //format of file info is:
        //firstName lastName phoneNumber
        string lineRead;
        string fName;
        string lName;
        string phoneNumber;
        string emailAddy;

        while(getline(readFile, lineRead)){
            stringstream ss(lineRead);
            ss >> fName >> lName >> phoneNumber >> emailAddy;

            //test that the file is getting read
            cout << fName << " "<< lName << " "
            << phoneNumber << " " << emailAddy;
        
        }

    }
    else if(userSelection == 3) {
        cout << "Sending all the emails!" << endl;

    }
    else {
        cout << "Please make a valid selection" << endl;
    }


    return 0;
}