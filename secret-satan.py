import csv
import random
import smtplib

login = 'email'
password = 'password'

SUBJECT = "RAPTURE NETWORK SECRET SOLSTICE"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(login, password)

reader = csv.reader(open('data.csv'))

details = {}
people = []

for row in reader:
    key = row[0]
    details[key] = row[1:]
    people.append(key)


def match(p):
    r = random.randint(0, (len(people)-1))
    if p != people[r]:
        return r
    else:
        return match(p)

def sendMail(name, r):

    receiver = details[name][0]

    message = f"""\
Subject: RAPTURE NETWORK SECRET SOLSTICE
To: {receiver}
From: RAPTURE NETWORK

Hello {name},

this is the rapturebot! thanks for joining the RAPTURE NETWORK SECRET SOLSTICE!

your recipient is: {people[r]}
address: {details[people[r]][1]}
email: {details[people[r]][0]}

how to:
send a gift to your recipient at the address listed above in the next 2 weeks
aim for around a £10 limit (that’s 11e, 13$, 18AUD, 1,385¥, 403THB) but honestly if you want to spoil someone rotten then go for it!

it could be...

a record from your collection…?
a CD from discogs…? (pro tip - choose a seller in your recipient’s country if cross border)
a download from bandcamp…?
a tape from ebay…?
something else entirely…!

any problems, please email: network4rapture@gmail.com

happy holidays, stay safe, trust in trance
love from rapture network

"""

    server.sendmail(login, receiver, message.encode('utf-8'))
    print ("email sent to "+name+" ("+receiver+") matched with "+people[r])


for name, detail in details.items():
    r = match(name)
    sendMail(name,r)
    people.pop(r)
