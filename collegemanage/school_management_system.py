import pyfiglet
class auth:
    def encode(self,strr):
        from sql import DbHelperauth

        d = DbHelperauth()
        return d.encode(strr)

    def decode(self,strr):
        from sql import DbHelperauth

        d = DbHelperauth()
        return d.decode(strr)

    def authh(role):
        from sql import DbHelperusers,DbHelperauth

        d = DbHelperauth()
        c = DbHelperusers()

        user   = input("Enter the user Name\n")
        passw  = input("Enter the password\n")
        s      = c.auth(user,role)

        if  s  ==  0:
            print("You are not in database")
            return False

        if passw == d.decode(s):
            return True
        return d

class msg:
    def adminfirst():
        print("*******     Tum karna kya cahate ho      **********\n")
        print("Press 1 for ADD teacher data")
        print("Press 2 for Show teacher data")
        print("Press 3 for Upload result")
        print("Press 4 for Check Update request")
        print("Press 5 for Logout")


    def fac():
        print("""Press 1 for teacher
Press 2 for Librarian
Press 3 for Accountant""")

class student:
    from sql import DbHelper_student

    def Displayassigment(self):
        pass


    def show_Test_date(self):
        pass


    def show_Results(self):
        pass


    def show_time_table(self):
        pass


    def show_attendance(self):
        pass


    def sendupdaterequest(self):
        print("Hello tum kya update karoge")


    def register(self):
        from sql import DbHelper_student
        t      = DbHelper_student()

        mobile = input("Enter mobile no\n")
        email  = input("Enter email id\n").lower()

        if t.auth(mobile,email)==True:
            from sql import DbHelperusers
            d     = DbHelperusers()
            en    = auth()
            passw = input("Enter your password")
            paa   = en.encode(passw)
            d.adduser(email,paa,"Student")
            print("register done")
                    
        else:
            print("Something went wrong")

class parents:
    from sql import DbHelper_parents

    def Performance_student(self):
        pass

    def contact_with_teacher(self):
        pass

    def show_due_fees(self):
        pass

class faculty(student):

    def show_student_info(self):
        print("Press 1 for search by srno")
        print("Press 2 for search by Name")
        print("Press 3 For search by Mobile no")
        print("Press 4 for search all student")

        choice = input()
        for i in range(3):
            if choice in ["1","2","3","4","5"]:
                choice = int(choice)
                break

            else:
                print("Enter a valid option")
                if i == 2:
                    print("You are Enter many time wrong option")
                    exit()
                choice = input()
        from sql import DbHelper_faculty
        f = DbHelper_faculty()

        if choice== 1:
            sr = int(input("Enter Sr. no"))
            f.showstudentdata(1,sr)

        elif choice== 2:
            sr = input("Enter Sr. no")
            f.showstudentdata(2,sr)

        elif choice== 3:
            sr = input("Enter Sr. no")
            f.showstudentdata(3,sr)

        elif choice== 4:
            f.showstudentdata(4)

        else:
            print("Something went wrong")
        
    def Teachers(self,condi,option):
        if condi==True:
            if option==1:
                def add_student_info():
                    from sql import DbHelper_faculty
                    p = DbHelper_faculty()
                    emty = []
                    Name                =        input("Enter name\n").capitalize()
                    Fathername          =        input("Enter Fathername\n").capitalize()
                    Mothername          =        input("Enter mothername\n").capitalize()
                    Addre               =        input("Enter the Address\n").capitalize()
                    pincode             =        input("Enter pin code\n").capitalize()
                    dob                 =        input("Enter the DOB Format DD-MM-YYYY\n")
                    mobileno            =        input("Enter the mobile no\n").capitalize()
                    email               =        input("Enter the email\n").lower()
                    gender              =        input("Enter the gender\n").capitalize()
                    category            =        input("Enter category\n").capitalize()
                    course              =        input("Enter course\n").capitalize()
                    Department          =        input("Enter Department\n").capitalize()
                    Addmission          =        input("Enter Addmision Year\n").capitalize()
                    # emty.append(Name,Fathername,Mothername,Addre,pincode,dob,mobileno,email,gender,category,course,Department,Addmission)
                    # for index,i in enumerate(emty):
                    #     if i=="":
                    #         print("Please Give a value")
                    #         val = input()
                    #         emty[index] = val
                    #         if ""==emty[7]:
                    #             re

                    p.addstudentdata(Name,Fathername,Mothername,Addre,pincode,dob,mobileno,email,gender,category,course,Department,Addmission)
                add_student_info()
            elif option==3:
                from sql import DbHelper_faculty
                p = DbHelper_faculty()
                p.uploadassgiment()

        elif condi==False:

            if option==1:
                from sql import DbHelper_faculty

                t      = DbHelper_faculty()

                mobile = input("Enter mobile no")
                email  = input("Enter email id").lower()

                if t.auth(mobile,email)==True:
                    from sql import DbHelperusers
                    d     = DbHelperusers()
                    en    = auth()
                    passw = input("Enter your password")
                    paa   = en.encode(passw)
                    d.adduser(email,paa,"Teacher")
                    print("register done")
                    
        else:
            print("Something went wrong")

    def Librarian(self):
        pass

    def Accountant(self):
        pass

class admin(faculty,parents,student):

    def show_teacher_data(self):
        from sql import DbHelper_admin

        d = DbHelper_admin()

        print("search by Name or teacher id")
        print("""Press 1 for all teacher data
Press 2 for Name
Press 3 for mobile no""")

        choice = input()
        
        if choice in ["1","2","3"]:
            choice = int(choice)

        else:
            print("Please Enter vaild option")
            exit()

        if choice==1:
            d.showteacherdata(choice)
        
        elif choice==2:
            naam = input("Enter the name\n")
            d.showteacherdata(choice,naam)

        elif choice==3:
            naam = input("Enter the Mobile no\n")
            d.showteacherdata(choice,naam)

    def check_change_request(self):
        pass

    def fill_student_result(self):
        pass

    def add_teacher_data(self):
        from sql import DbHelper_admin

        d = DbHelper_admin()

        name       = input("Enter first name\n").capitalize()
        father     = input("Enter father name\n").capitalize()
        subject    = input("Enter the suject\n").capitalize()
        department = input("Enter the department\n").capitalize()
        mobile     = input("Enter the mobile\n")
        emailid    = input("Enter the email id\n").lower()

        d.addteacher(name,father,subject,department,mobile,emailid)

def main():
    cho = input("""Choice for login
    Press 0 for Exit
    Press 1 for Student
    Press 2 for Parents
    Press 3 for Faculty
    Press 4 for Admin\n
    Option : """)

    if cho in ["0","1","2","3","4"]:
        cho = int(cho)

    else:
        print("Select Vaild option")
        exit()

    if cho==0:
        exit()
        
    elif cho==1:  # For Student
        print(pyfiglet.figlet_format("STUDENT   LOGIN"))
        d    = auth.authh("Student")
        if d == True:
            pass

        elif d == False:
            print("Press 1 for Register")
            print("Press 2 for main login page")
            print("Press 3 for exit")
            
            cho  = input()
            if cho in ["1","2","3"]:
                cho = int(cho)
            else:
                print("Please select a vaild option")
                exit()
            if cho ==1:
                fe = student()
                fe.register()
            elif cho ==2:
                main()
            elif cho ==3:
                exit()
            else:
                print("something went wrong")
    elif cho==2: # For Parents 
        print(pyfiglet.figlet_format("PARENTS   LOGIN"))
        d    = auth.authh("Parents") 

    elif cho==3: # For Faculty
        print(pyfiglet.figlet_format("FACULTY   LOGIN"))
        msg.fac()
        cho = input()

        for i in range(3):  # For give  3 chance
            if cho in ["1","2","3"]:
                cho = int(cho)

                break

            else:
                print("Enter a valid option")
                if i == 2:
                    print("You are Enter many time wrong option")
                    exit()
                cho = input()

        if cho==1:
            print(pyfiglet.figlet_format("TEACHER   LOGIN"))
            d      = auth.authh("Teacher")

            if d   == True:
                fe = faculty()
                print("Press 1 For Upload student data")
                print("Press 2 For Show student data")
                print("Press 3 for Upload assginment")
                print("Press 4 for Show assginment")
                print("Press 5 For Upload Ct or Exam date")
                print("Press 6 For Show Ct or Exam date")
                print("Press 7 For Upload Student Attendance")
                print("Press 8 For Show Student Attendance")
                print("Press 9 For Show Profile")
                print("Press 10 For Check Student Profile Update Reqest")
                print("Press 11 For Logout")
                cho = input()

                for i in range(3):  # For give  3 chance
                    if cho in ["1","2","3","4","5","6","7","8","9","10","11"]:
                        cho = int(cho)

                        break
                    
                    else:
                        print("Enter a valid option")
                        if i == 2:
                            print("You are Enter many time wrong option")
                            exit()
                        cho = input()

                if cho==1:
                    fe.Teachers(True,1)

                elif cho==2:
                    fe.show_student_info()

                elif cho==3:
                    fe.Teachers(True,3)

                elif cho==4:
                    pass

                elif cho==5:
                    pass

                elif cho==6:
                    pass

                elif cho==7:
                    pass

                
                elif cho==8:
                    pass

                elif cho==9:
                    pass

                elif cho==10:
                    pass

                elif cho==11:
                    main()

                else:
                    print("Something went wrong")
                    exit()

            elif d == False:

                print("Press 1 for Register")
                print("Press 2 for main login page")
                print("Press 3 for exit")
                
                cho  = input()

                if cho in ["1","2","3"]:
                    cho = int(cho)

                else:
                    print("Please select a vaild option")
                    exit()

                if cho ==1:
                    fe = faculty()
                    fe.Teachers(False,1)

                elif cho ==2:
                    main()

                elif cho ==3:
                    exit()

                else:
                    print("something went wrong")

    elif cho==4: # Admin Login
        print(pyfiglet.figlet_format("ADMIN   LOGIN"))
        d   = auth.authh("Admin")
        if d==True:
            msg.adminfirst() # pop up msg from msg class
            choice = input()
            for i in range(3):
                if choice in ["1","2","3","4","5"]:
                    choice = int(choice)
                    break

                else:
                    print("Enter a valid option")
                    if i == 2:
                        print("You are Enter many time wrong option")
                        exit()
                    choice = input()

            if choice==1:
                ad = admin()
                ad.add_teacher_data()

            elif choice==2:
                ad = admin()
                ad.show_teacher_data()

            elif choice==3:
                pass

            elif choice==4:
                pass
            
            elif choice==5:
                main()

            else:
                print("Something went wrong")

        elif d==0:
            print("Kindly contact Admin")
            exit()

        else:
            print("you write wrong password")
            print("Press 1 for Forget password")
            print("Press 2 for Exit")
            
            cho = input()
            
            if cho in ["1"]:
                cho = int(cho)

            else:
                print("select a vaild option")
                exit()

            if cho   ==  1:
                from sql import DbHelperusers
                d    = DbHelperusers()
                user = d.updatepassword(input("Enter email id").lower())

                if user==True:
                    print("Password updated")

                elif user ==None:
                    print("Please Enter valid otp or you can't in database")

                else:
                    print("Something went worng")

    else:
        print("Somthing went wrong try again")

if __name__ == "__main__":
    main()