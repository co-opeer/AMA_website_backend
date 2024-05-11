import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(sender_email, app_password, receiver_email, subject, message):
    # Check if Less Secure Apps is enabled (recommended alternative: use SendGrid)
    # ... (consider adding a check and warning if Less Secure Apps is enabled)

    # Connect to SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, app_password)  # Use App Password here

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message content
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    smtp_server.send_message(msg)

    # Close connection
    smtp_server.quit()





def send_email(receiver_email, url, result):
    sender_email = "ama.opticore@gmail.com"
    subject = "Результат для зображення"
    app_password = "pzsp svfl kvdd dzpv"
    message = f"Зображнння: {url}, \n Результат: {result}"

    send(sender_email, app_password, receiver_email, subject, message)



