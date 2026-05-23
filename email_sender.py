import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
EMAIL = "1234example@gmail.com"
APP_PASSWORD = "your_app_password_here"

# Read message from file
with open("message.txt", "r") as file:
    MESSAGE = file.read()

# Read recipients from file
with open("recipients.txt", "r") as file:
    recipients = file.readlines()

def send_emails():
    try:
        # SMTP Server Setup
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login
        server.login(EMAIL, APP_PASSWORD)

        # Send email to each recipient
        for recipient in recipients:
            recipient = recipient.strip()

            msg = MIMEMultipart()
            msg["From"] = EMAIL
            msg["To"] = recipient
            msg["Subject"] = "Automated Email from Python"

            msg.attach(MIMEText(MESSAGE, "plain"))

            server.sendmail(EMAIL, recipient, msg.as_string())

            print(f"Email sent to {recipient}")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print("Error:", e)