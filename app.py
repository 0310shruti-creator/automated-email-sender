from flask import Flask, render_template,request, redirect, url_for
from email_sender import send_emails

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    success = None
    error = None


    if request.method == "POST":

        recipients = request.form["recipients"].split(",")
        subject = request.form["subject"]
        message = request.form["message"]

        send_emails(recipients, subject, message)


        try:
            send_emails(recipients, subject, message)
            return redirect(url_for("success"))
        
        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")

@app.route("/success") 
def success(): 
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)