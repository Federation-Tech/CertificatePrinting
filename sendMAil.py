import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "fed@kiitincubator.in"
email_list = ["2030031@kiit.ac.in"]

# Define the password (better to reference externally)
# As shown in the video this password is now dead, left in as example only
pswd = "jmgoraovwsorejyl"


# name the email subject
subject = "Heartfelt thank you for your participation from FED societyHeartfelt thank you for your participation from FED society"

# Define the email function (dont call it email!)


def send_emails(email_list):

    for person in email_list:

        # Make the body of the email
        body = f"""Dear Seniors,
        The FED Society would like to extend sincerest gratitude for your participation, support, and guidance during our recent event. 
        As seniors ,your presence, valuable insights, and precious time were truly invaluable, and we are deeply grateful for your contributions.Your guidance and support have been instrumental in ensuring the success of the event. 
        Once again, we would like to express our deepest gratitude and admiration for your hard work, guidance, and dedication. We look forward to continuing to work with you in the future if possible and make positive impact together.
        Warm Regards,

        FEDKIIT Team
        """

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "Aayasha A.Naya.png"

        # Open the file in python as a binary
        attachment = open(filename, 'rb')  # r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header(
            'Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()


# Run the function
send_emails(email_list)
