from flask import Flask , render_template , request , redirect
import csv
app = Flask(__name__)

@app.route("/")
def html_file():
    return render_template('index.html')

@app.route("/MessageSent")
def redirect_file():
    return render_template('redirect.html')


def write_to_database(data):
    with open('database.csv' ,mode='a' ,newline='') as db:
        Name=data['Name']
        Email=data['Email']
        Message=data['Message']
        csv_writer= csv.writer(db,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Name, Email , Message])

@app.route("/submit_message" , methods=['POST' , 'GET'])
def submit_msg():
    try:
        if request.method=='POST':
            data=request.form.to_dict()
            write_to_database(data)
            return redirect('/MessageSent')
    except:
        return 'Something went wrong  !'
    