from flask import Flask , render_template , request , redirect
import csv
import smtplib 
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def html_file():
    return render_template('index.html')

@app.route("/MessageSent")
def redirect_file():
    return render_template('redirect.html')


def sendmail(data):
        Name=data['Name']
        Email=data['Email']
        Message=data['Message']

        email = EmailMessage()  # Instantiate a email object from EmailMessage class.


        email['From'] = Email

        email['To'] = "vernnit@gmail.com"

        email['Subject'] = Name

        email.set_content(Message)


        # Login to gmail using smtp server
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()

        smtpserver.login('andreihoward603@gmail.com', 'rwov kzvk zxge xize')

        smtpserver.send_message(email)



@app.route("/submit_message" , methods=['POST' , 'GET'])
def submit_msg():
    try:
        if request.method=='POST':
            data=request.form.to_dict()
            sendmail(data)
            return redirect('/MessageSent')
    except:
        return 'Something went wrong  !'
    