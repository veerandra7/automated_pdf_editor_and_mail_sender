# automated_pdf_editor_and_mail_sender

  1.Go through "Task description.txt" file for clear understanding of task

# Description of code:
  1. app.py file has the whole pipeline.
  2. convert.py module is built with all functions needed for conversion and extraction of data from binary and, to create subject for each mail.
  3. mailsender.py module is for configuring your email id with smtplib for sending mails. Also, it has subject and body required for mail.
  4. pdf_convert.py module is for attaching logo and texts on pdf based on location. "output_email_attachment.pdf" is the example for this

# How to run:
  1. Create environment with the help of 'environment.yml' file, with the command below 
      "conda env create -f environment.yml"
  2. configure your email id(gmail) and password in "mailsender.py" file.
  3. Make sure that your privacy setting in gmail is turned ON to “Less secure apps”.
  4. Now, run "app.py"
  5. The mails with attachments,subject and body will be sent to the mails present in "input_data.xlsx"

 
