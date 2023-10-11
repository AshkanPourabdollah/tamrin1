"""
This is a Flask project 
Programmed by ashkan pourabdollah
"""
from flask import Flask,render_template
import texts

app=Flask("app")
"""-------------------------------------------------------------------------------------------------------"""
# this is a first page of our project
@app.route("/")
def index():

    context={"title":"اشکان پورعبدالله",
             "body":texts.index_text}
    
    return render_template("main.html",data=context)

"""-------------------------------------------------------------------------------------------------------"""
# this is about our team
@app.route("/about")
def about():

    context={"title":"درباره ی ما",
             "body":texts.about_text}
    
    return render_template("main.html",data=context)

"""-------------------------------------------------------------------------------------------------------"""
# this is contact us page
@app.route("/contact")
def contact():

    context={"title":"تماس با ما",
             "body":texts.contact_text}
    
    return render_template("main.html",data=context)

"""-------------------------------------------------------------------------------------------------------"""
app.run()

