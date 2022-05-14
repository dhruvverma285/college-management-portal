import mysql.connector as connector
class DbHelper_student:
    def __init__(self):
        self.con=connector.connect(
                                    host     = 'localhost',
                                    database = 'studentms',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )

    def auth(self,mobile,email):

        query = f"select Email,Mobile_no from bcastudent Where Email='{email}' and Mobile_no = '{mobile}';"
        cur   = self.con.cursor()
        cur.execute(query)

        for i in cur:
            if email==i[0] and mobile==i[1]:
                from otpgen import otpgen,sendmail
                otp = otpgen()
                sendmail(otp,email)
                op = int(input("Enter the Otp"))
                if otp==op:
                    return True
                else:
                    print("Your Otp are invaild")
                    return "missotp"

        else:
            return False

class DbHelper_parents:
    def __init__(self):
        self.con=connector.connect(
                                    host     = 'localhost',
                                    database = 'studentms',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )


class DbHelper_faculty:
    def __init__(self):

        self.con=connector.connect(
                                    host     = 'localhost',
                                    database = 'studentms',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )
    def auth(self,mobile,email):

        query = f"select Email,Mobile_no from addteacherdata Where Email='{email}' and Mobile_no = '{mobile}';"
        cur   = self.con.cursor()
        cur.execute(query)

        for i in cur:
            if email==i[0] and mobile==i[1]:
                from otpgen import otpgen,sendmail
                otp = otpgen()
                sendmail(otp,email)
                op = int(input("Enter the Otp"))
                if otp==op:
                    return True
                else:
                    print("Your Otp are invaild")
                    return "missotp"

        else:
            return False

    def addstudentdata(self,Name,Father,Mother,address,pin,Dob,Mobile,Email,Gender,Category,Course,Department,Addmissionyear):
        query = "CREATE TABLE if not exists bcastudent(Sr_no INT NOT NULL AUTO_INCREMENT,Name VARCHAR(45) NOT NULL, Father_name VARCHAR(45) NOT NULL,Mother_name VARCHAR(45) NOT NULL, Address VARCHAR(45) NOT NULL,Pincode VARCHAR(6) NOT NULL,Dob VARCHAR(45) NOT NULL,Mobile_no VARCHAR(10) NOT NULL,Email VARCHAR(45) NULL,Gender VARCHAR(1) NOT NULL,Category VARCHAR(4) NOT NULL,Course VARCHAR(45) NOT NULL,Department VARCHAR(45) NOT NULL,Addmission_Year VARCHAR(4) NOT NULL,  PRIMARY KEY (Sr_no),  UNIQUE INDEX Mobile_no_UNIQUE (Mobile_no ASC) VISIBLE,  UNIQUE INDEX Email_UNIQUE (Email ASC) VISIBLE);"
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()

        query = f"Insert into bcastudent(Name,Father_name,Mother_name,Address,Pincode,Dob,Mobile_no,Email,Gender,Category,Course,Department,Addmission_Year) values('{Name}','{Father}','{Mother}','{address}','{pin}','{Dob}','{Mobile}','{Email}','{Gender}','{Category}','{Course}','{Department}','{Addmissionyear}');"
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()
    def showstudentdata(self,choice,naa=None):

            if choice == 1:
                query = f"select * from bcastudent Where Sr_no='{naa}';"
                cur   = self.con.cursor()
                cur.execute(query)
                for x in cur:
                    print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]},{x[7]},{x[8]},{x[9]},{x[10]},{x[11]},{x[12]},{x[13]}')
            
            elif choice == 2:
                query = f"select * from bcastudent Where Name='{naa}';"
                cur   = self.con.cursor()
                cur.execute(query)
                for x in cur:
                    print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]},{x[7]},{x[8]},{x[9]},{x[10]},{x[11]},{x[12]},{x[13]}')
           
            elif choice == 3:
                query = f"select * from bcastudent Where Mobile_no='{naa}';"
                cur   = self.con.cursor()
                cur.execute(query)
                for x in cur:
                    print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]},{x[7]},{x[8]},{x[9]},{x[10]},{x[11]},{x[12]},{x[13]}')
          
            elif choice == 4:
                query = f"select * from bcastudent;"
                cur   = self.con.cursor()
                cur.execute(query)
                for x in cur:
                    print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]},{x[7]},{x[8]},{x[9]},{x[10]},{x[11]},{x[12]},{x[13]}')
           
            else:
                print("Something wrong")
    

    def uploadassgiment(self,teachername=None,Uploaddate=None,lastdate=None,question=None):
        self.con        =           connector.connect(
                                    host     = 'localhost',
                                    database = 'assigment',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )

        query = "drop table test"
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()

class DbHelper_admin:

    def __init__(self):

        self.con=connector.connect(
                                    host     = 'localhost',
                                    database = 'studentms',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )

    def addteacher(self,name,father,subject,department,mobile,emailid=None):
        query = 'create table if not exists addteacherdata(Teacher_id INT NOT NULL AUTO_INCREMENT,Name VARCHAR(45) NOT NULL,Father_name VARCHAR(50) NOT NULL,Subject VARCHAR(50) NOT NULL,depart VARCHAR(50) NOT NULL,Mobile_no VARCHAR(50) NOT NULL,Email VARCHAR(50) NOT NULL,PRIMARY KEY (Teacher_id),UNIQUE INDEX Teacher_id_UNIQUE(Teacher_id ASC) VISIBLE,UNIQUE INDEX Mobile_no_UNIQUE (Mobile_no ASC) VISIBLE,UNIQUE INDEX Email_UNIQUE (Email ASC) VISIBLE);'
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()

        query = "insert into addteacherdata(Name,Father_name,Subject,depart,Mobile_no,Email) values('{}','{}','{}','{}','{}','{}')".format(name,father,subject,department,mobile,emailid)
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()
            
       
    def showteacherdata(self,choice,naa=None):

        if choice == 1:
            query = "select * from addteacherdata;"
            cur   = self.con.cursor()
            cur.execute(query)

            for x in cur:
                print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]}')


        elif choice == 2:
            query   = f"select * from addteacherdata where Name='{naa}';"
            cur     = self.con.cursor()
            cur.execute(query)

            for x in cur:
                print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]}')


        elif choice == 3:
            query   = f"select * from addteacherdata where Mobile_no='{naa}';"
            cur     = self.con.cursor()
            cur.execute(query)

            for x in cur:
                print(f'{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]}')

    def upload_result(self):
        pass

    def check_change_request(self):
        pass

    def data(self):
        query = "select * from addteacherdata;"
        cur   = self.con.cursor()
        cur.execute(query)
        c = []
        for i in cur:
            c.append(i)
        return c


class DbHelperusers:
    def __init__(self):
        self.con=connector.connect(
                                    host     = 'localhost',
                                    database = 'collegeuser',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )
    
    def auth(self,user,role):
        query = f"select * from usersdata where Role='{role}'"
        cur   = self.con.cursor()
        cur.execute(query)
        username = 0
        for i in cur:
            if user==i[1]:
                return i[2]  
        return username

    def adduserforadmin(self,user,passw,role):
        query = f"insert into usersdata(Username,Password,Role) values('{user}','{passw}','{role}');"
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def adduser(self,user,passw,role):
        query = f"insert into usersdata(Username,Password,Role) values('{user}','{passw}','{role}');"
        cur   = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def updatepassword(self,email):
        from otpgen import otpgen,sendmail
        otp = otpgen()
        sendmail(otp,email)
        op = int(input("Enter the Otp"))
        if otp ==op:
            d     = DbHelperauth()
            passw = d.encode(input("Enter new Password"))
            query = f"update usersdata set Password = '{passw}' where Username='{email}';"
            cur   = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            return True
        else:
            return None
        

class DbHelperauth:   # For key auth encrypt and decrypt password
    
    def __init__(self):
        self.con=connector.connect(
                                    host     = 'localhost',
                                    database = 'bros',
                                    user     = 'root',
                                    password = 'Boss123@12345',
                                    )
        self.key = self.key()

    def encode(self,strr):
        from cryptography.fernet import Fernet

        strr       = bytes(strr,'utf-8')
        fernet     = Fernet(self.key)
        encmassage = fernet.encrypt(strr)
        d          = str(encmassage).split("'")[1]

        return d

    def decode(self,strr):
        from cryptography.fernet import Fernet
        strr       = bytes(strr,'utf-8')
        fernet     = Fernet(self.key)
        decmassage = fernet.decrypt(strr)
        d          = str(decmassage).split("'")[1]
        return d

    def key(self):
        query = "select * from userk where name='admin';"
        cur   = self.con.cursor()
        cur.execute(query)

        for i in cur:
            query= i[2]
        f     = bytes(query,'utf-8')
        return f