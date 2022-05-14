def otpgen():
    import random
    a = ["0","1","2","3","4","5","6","7","8","9"]
    otp = []
    for i in range(6):
        otp.append(random.choice(a))
    otp = "".join(otp)
    return int(otp)


def sendmail(body,to):
    import smtplib as s
    """"This funtion is send mail to other"""
    # with open("C:\\boss\\New folder\\pass.txt","r") as e:
    #     emailpass = e.read()
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("otpgen123@gmail.com","XqZaWPJmFP")
    message= f"Subject:This mail for send a otp from prashant Project\n\nPlese enter this otp for veryfication : {body}"
    ob.sendmail("otpgen123",to,message)
    ob.quit()
    print("OTP SENT")

