import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import datetime
import pandas as pd

from dateutil import parser
currentDate = datetime.date.today()
sheet_name = currentDate.strftime("%B-%Y")
filename =datetime.datetime.today().strftime('%m-%d-%Y')
filename1 = 'Airfi_' + str(format(filename))
sheet_id = "19SzfcL3muVeISycG5eFYUqwrwwReGETZsNtl-euG71U"
#sheet_name = "October-2022"

url=f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
print(url)

today = pd.to_datetime("today").strftime("%Y-%m-%d")
yesterday = (pd.to_datetime("today") - pd.Timedelta(1, unit='D')).strftime("%Y-%m-%d")

df = pd.read_csv(url)

df['temp_date'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%dT%H:%M:%S.%fZ')
filtered_df = df.loc[(df['temp_date'] >= yesterday) & (df['temp_date'] < today )]

#print(filtered_df)
#filtered_df.to_csv(open(filename1+'.csv' ,'w'), header = True, index=False)
filtered_df.to_csv(open(filename1+'.csv','w'), header = True, index=False)

#fromaddr = "noreply@airarabia.com"
#toaddr = ["rverma@airarabia.com", "mraes@isa.ae", "pmangal@airarabia.com","rifath.jm@isa.ae"]

#msg = MIMEMultipart()

#msg['From'] = fromaddr
#msg['To'] = ', '.join(toaddr)
#msg['Subject'] = "Airfi Data"

#body = "Daily Airfi Data"

#msg.attach(MIMEText(body, 'plain'))


#attachment = open('/home/francis/desktop/'+filename1+'.csv', "rb")


#part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', "attachment; filename= %s" % filename1+'.csv')

#msg.attach(part)

#server = smtplib.SMTP('10.200.22.64', 25)
#server = smtplib.SMTP('10.200.2.93', 25)

#text = msg.as_string()
#server.sendmail(fromaddr, toaddr, text)
#server.quit()

