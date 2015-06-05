#Disease simulation model with python_Website

#Importation of the modules needed
from flask import Flask
from flask import render_template

app = Flask(__name__)

#Creation of the different ways needed for my views, they correspond to the number of items
#in my menu.
@app.route('/home')
def home():
    return render_template('skeleton.html')
	
@app.route('/models')
def models():
    return render_template('skeleton_models.html')
	
@app.route('/application')
def application():
    return render_template('skeleton_appli.html')
	
@app.route('/contacts')
def contacts():
    return render_template('skeleton_contact.html')
	
#Debug is needed to run the code, it helps me to detect mistakes in my code. Given the website
#won't be on the internet, I can keep it that way.	
if __name__ == '__main__':
    app.run(debug=True)