import mysql.connector as connector
from cryptography.fernet import Fernet
class DbHelperusers:
    def __init__(self):
        self.con=connector.connect(
                                    host='localhost',
                                    database='BROS',
                                    user='root',
                                    password='Boss123@12345',
                                    )

    def inser(self,name,key):
        query = f"insert into userk(name,userkname) values('{name}','{str(key)}');"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

password = "Lacy5061@"
password = bytes(password,'utf-8')
key = Fernet.generate_key()
fernet = Fernet(key)
encmessage = fernet.encrypt(password)
decmessage = fernet.decrypt(encmessage)
h = str(key)
h = h.split("'")

print(encmessage)
print(decmessage)
d = DbHelperusers()
d.inser("admin",h[1])
print(h[1])