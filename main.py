from flask import Flask, request, redirect, render_template
import getpass

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST","GET"])
def validate_fields():
    error_string_username=""
    error_string_password=""
    error_string_validate_password = "" 
    error_string_email=""
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        validate_password = request.form['validate_password']
        email = request.form['email']
        isError = False

        if not username or len(username) < 3 or len(username) > 20 or " " in username:
            username=""
            error_string_username = "Username is not valid!"
            isError = True
            #return redirect("/?username_error=" + username_error + "&username=" + username)
            
        if not password or len(password) < 3 or len(password) > 20 or " " in password:
            error_string_password = "Password is not valid!" 
            isError = True
            
        if not validate_password or validate_password == " " or password != validate_password:
            error_string_validate_password = "Passwords do not match!" 
            isError = True
            
        if '@' not in email or '.' not in email or len(email) < 3 or len(email) > 20 or " " in email:
            email=""
            email_error = "That's not a valid email"
            error_string_email = "Email is not valid!"
            isError= True
            #return redirect("/?email_error=" + email_error + "&email=" + email)
        if isError == True:
            #return redirect(error_string)
            return render_template('user-signup.html', username=username, email=email, username_error=error_string_username, password_error=error_string_password, validate_password_error=error_string_validate_password, email_error=error_string_email)
        else:
            return render_template('welcome.html', username=username, email=email)
    else:
        return render_template('user-signup.html', username="", email="", password="", validate_password="")

'''@app.route("/")
def index():
    encoded_username = request.args.get("username")
    encoded_email = request.args.get("email")
    encoded_username_error = request.args.get("username_error")
    encoded_password_error = request.args.get("password_error")
    encoded_validate_password_error = request.args.get("validate_password_error")
    encoded_email_error = request.args.get("email_error")
    return render_template('user-signup.html', username=encoded_username, email=encoded_email,  username_error="", password_error=encoded_password_error, validate_password_error=encoded_validate_password_error, email_error=encoded_email_error)
'''
app.run()