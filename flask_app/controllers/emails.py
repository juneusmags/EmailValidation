
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Email





@app.route("/")
def index():
    return render_template("email.html")


@app.route("/submit", methods = ["POST"])
def submit():

    if not Email.validate_email(request.form):
        return redirect("/")

    mysql = connectToMySQL("email_val")
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW())"
    data = {
        "email" : request.form["email"]
    }
    mysql.query_db(query, data)
    return redirect ("/success")



@app.route("/success")
def suceess():
    mysql = connectToMySQL("email_val")
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template("success.html", all_emails = emails)
