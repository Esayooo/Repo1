s =' Hello,everyone.My name is Ersanat.123 23 !'
def str():
    alpha=0
    san=0
    bos=0
    symbol=0
    for i in s:
        if i.isdigit():
            san +=1
        elif i.isspace():
            bos +=1
        elif i.isalpha():
            alpha +=1
        else:
            symbol +=1
    print(f'Жолдағы сандар саны {san}')
    print(f'Жолдғы бос орындар саны {bos}')
    print(f'Жолдғы әріптер саны {alpha}')
    print(f'Жолдғы символдар саны {symbol}')
    print(s.upper())
    print(s.lower())
str()

def replace():
    print(s.replace('e','i',2))
replace()
def count():
    c=s.count('x')
    print(f'Жолдағы"X" әріп саны {c}')
count()

def strip():
    print(s.strip('!'))

strip()

# print(text.isalpha())#检查是不是都是字符串
# print(Information.capitalize())#将字符串首字母大写
# print(text.title())#标题大写


