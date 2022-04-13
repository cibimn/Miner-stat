import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def watchdog():
    url = "https://api.ethermine.org/miner/B21987285d8D828c7f24722E1350732913788f11/dashboard"
    response = requests.get(url)
    if response.status_code != 200:
        print('error {}'.format(response.status_code))
    else:
        data = json.loads(response.text)
        #print(json.dumps(data, indent=4))
        last_data = (data['data']['statistics'])[-1]
        hashrate = round(last_data['reportedHashrate']/1000000)
        print(hashrate)
    if hashrate < 260:
        email(hashrate)


def email(hash):
    print(hash,'hashrate')
    mail_content = "Hashrate Low: "+str(hash)+""
    sender_address = 'nmanivcb@gmail.com'
    sender_pass = '4HiBUB#Ncb'
    receiver_address = 'cibimn@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Hashrate Alert'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

if __name__ == "__main__":
    watchdog()