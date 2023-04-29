from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_database(data):
    with open('database.txt', 'a') as my_data:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = my_data.write(f'\nemail: {email}, subject: {subject}, message: {message}')


def write_to_csv(data):
    with open('/home/JulesLancz/protfo/database.csv', 'a', newline='') as my_data2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(my_data2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'
