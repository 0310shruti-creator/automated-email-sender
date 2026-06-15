import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials (email and app password)
EMAIL = "0310shruti@gmail.com"
APP_PASSWORD = "xhvu seub ajsj zghq"

def send_emails(recipients, subject, message):
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

            msg.attach(MIMEText(message, "plain"))

            server.sendmail(EMAIL, recipient, msg.as_string())

            print(f"Email sent to {recipient}")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print("Error:", e)
