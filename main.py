from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('./database.txt','a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        text = file.write(f'\nemail: {email}, subject: {subject}, message: {message}')
        

def write_to_csv(data):
    with open('./database.csv','a') as file2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(file2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# @app.route('/submit_form', methods=['POST', 'GET'])      #1st Way
# def submit_form():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         subject = request.form.get('subject')
#         message = request.form.get('message')
#         li = [email,subject,message]
#         with open('./database.txt',mode='a') as file:
#             file.write(f'\nemail: {email}, subject: {subject}, message: {message}')
#         print(li)
#         return redirect('/thankyou.html')
#     else:
#         return 'something went wrong!!'
    
@app.route('/submit_form', methods=['POST', 'GET'])         #2nd Way
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to the database!!'
    else:
        return 'something went wrong!!'