import random
import string


digitnum = int(input("How many digits do you want your password?"))
symbols = "!@#$%^&*()_+{}|:<>?-=[]\;',./'"
thepassword = []
x = 0

while x != digitnum:
    thepassword.append(random.randrange(0, 11))
    thepassword.append(random.choice(string.ascii_letters))
    thepassword.append(random.choice(symbols))
    x += 1

listToStr = ''.join([str(elem) for elem in thepassword])
thepassword = listToStr

print(thepassword)

