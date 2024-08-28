import random

def CaptchaCheck(captcha, user_captcha):
    if captcha == user_captcha:
        return True
    return False

def CaptchaGenerator(n):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    captcha = ""

    captcha += chrs[random.randint(1, 1000) % 62]
    n = 1
    return captcha

captcha = CaptchaGenerator(9)
print("CAPTCHA IS :  ", captcha)

print("ENTER above CAPTCHA")
usr_captcha = input()

if(CaptchaCheck(captcha, usr_captcha)):
    print("The CAPTCHA is Matched here...")
else:
    print("The CAPTCHA is not Matched here...")


