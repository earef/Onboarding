
#Class Validation with Initialization method for
# user data collection & Redirection method to check
# user availability and domain check

class Validation:

    def __init__(self,List_Of_Users=None):  #Initial method with unconditional list (None) an empty list also valid
        self.List_Of_Users=List_Of_Users if List_Of_Users is not None else []
        Condition="yes"      #While loop for adding list of user enteries in a row
        while Condition=="yes":
            print("Enter the First Name:")
            FirstName = input()

            print("Enter the Last Name:")
            LastName = input()

            UserName = FirstName + '.' + LastName
            print("UserName: " + UserName)

            print("Enter the Domain without @ :")
            Domain = input()
            Email = FirstName + '.' + LastName + "@" + Domain
            print("Email Address:" + Email)
            self.List_Of_Users.append([FirstName, LastName, UserName, Domain, Email])  #Appending entery data to an existing list
            print("Do you want to add another user ? yes/no ")  #Yes;enables the while loop to add more User Login info , No;breaks the Condition of loop
            Condition=input()

    def Redirection(self):
          #This Method checks the validity of user and domains which user belong to it.
             #checking data proccess comes from the list of
               #user name as a input TBC
                 #user doesn't exist TBC
         print("Please give the username to check its Domain(username is Case Sensitive):")
         UsernameInput=input()
         for i in range(len(self.List_Of_Users)):
             if self.List_Of_Users[i][2]==UsernameInput:
                 #takes the 3rd value of matrix "List_Of_Users" compares with 4th value which is domain of user
                   #prints all Domains which reserved for the user
                 print(self.List_Of_Users[i][3])

