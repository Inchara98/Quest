import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os


def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body text to the email
    msg.attach(MIMEText(body, 'plain'))

    # If an attachment is provided, attach it to the email
    # if attachment_path:
    #     with open(attachment_path, "rb") as attachment:
    #         part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
    #         part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
    #         msg.attach(part)

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    # Replace these values with your actual email credentials and recipient's email address
    sender_email = "inchara.gowda@tibilsolutions.com"
    sender_password = "inchara98$"
    receiver_email = "incharakgowda1998@gmail.com"
    subject = "Selenium Test Execution Report"
    body = "Please find the attached Selenium test execution report."

    # Replace this with the actual path to your generated execution report
    execution_report_path = "Reports/report.html"

    # Sending the email with the execution report as an attachment
    send_email(sender_email, sender_password, receiver_email, subject, body, execution_report_path)
