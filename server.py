from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')   
    
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')     

# @app.route('/components.html')
# def components():
#     return render_template('components.html')     

# @app.route('/works.html')
# def works():
#     return render_template('works.html')  

# dynamically create external page link 
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)
           

# recieve information from 'form' element
# 'get' used in 'action' attribute of 'form' element to send user information by attaching to the URL
# 'post' used in 'method' attribute to get the information from the input
# the 'route funtction' used in the 'action' attribute of the 'form'
# assigning 'name' to the inputs within 'form' will show them in 'Form Data' of the 'route' in the 'Network'
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	# the values in 'Form Data' are accessed for the 'method' 'post'
    if request.method == 'POST':
        # request.form.['email'] gets only the data within the 'name' attribute
        # gets all the input data in form to a dictionary in the terminal
        data = request.form.to_dict()

        # append the data in the form the 'database.txt' file
        # write_to_file(data)

        # append the data in the form the 'database.txt' file
        write_to_csv(data)
        # 'redirect' module to return 'thankyou.html' file
        return redirect('/thankyou.html')
    else:
    	return 'something went wrong!'

# write the input data in contact form in the database file
def write_to_file(data):    	
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		# the data has to be written and stored in a variable
		file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		# csv writer configuration
		# 'newline' creates a new line for every time data is being input
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		# 'writerow' object takes the variables and places them in a row
		csv_writer.writerow([email,subject,message])