from convert import *
from pdf_convert import *
from mailsender import sendmail
import pandas as pd


input_data = 'input_data.xlsx'


in_pdf_file = 'inputfile.pdf'
out_pdf_file = 'outputfile.pdf'
img_file = 'input_logo.jpg'


mails_bin = get_emailid_in_bin(input_data)

# To extract emails from binary data
emails=[]
for email in mails_bin:
    req_mail = get_mail_from_bin(email)
    email += email
    emails.append(req_mail)
    
subj_line_list = get_subject_line_list(input_data)

# Add logo and text to pdf

pdf_edit(in_pdf_file,out_pdf_file,img_file)

df1 = pd.read_excel(input_data)
cols = df1.columns

#Send email


if 'Status' not in cols:
    df1['Status'] = 'unsent'
elif 'Status' in cols:
    df1['Status'] = np.where(df1['Status'].isnull(),'unsent','sent')

for i in range(len(emails)):
    if df1['Status'].loc[i] == 'unsent':
        sendmail(emails[i], subj_line_list[i], subj_line_list[i][28:])
    df1['Status'].loc[i] = 'sent'
    df1.to_excel(input_data,index=False)


