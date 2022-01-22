import pandas as pd

def get_emailid_in_bin(excel):
    df = pd.read_excel(excel)
    df_emails = df[['email']]
    n = len(df_emails)
    mail_list = [(df_emails.loc[i])[0] for i in range(n)]
    return mail_list

def get_mail_from_bin(email_bin):
    email_out = ''
    bin_values = email_bin.split()
    for bin_value in bin_values:
        to_int = int(bin_value, 2)
        to_ascii_char = chr(to_int)
        email_out += to_ascii_char
    return email_out


def get_subject_line_list(data):
    subject_line_list=[]
    df = pd.read_excel(data)
    for i in range(len(df)):
        a = (df.loc[i]['User Name'].split()[0]).lower()
        b = str(df.loc[i]['Encoded Code'])
        subject_line = 'Your course material'+'_' + b + '_' + a
        subject_line_list.append(subject_line)
    return subject_line_list 

