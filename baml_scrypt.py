# Lassana DJIRE
'''
Ce script deplace les fichiers dont le nom commence par lass et  date de creation est egal a aujourd'hui dans un dossier 
le compresse et l envoi par mail.

'''
import os
import datetime
from datetime import date
import subprocess
import shutil
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging

def at_butget_jour():
    # definir le chemin de base
    a = '/Users/mac/Documents/projets/Scripts/test_1/'
    date_jour = date.today()
    # Non du repertoire atbudget
    name_dir = "atbudget_%s_%s_%s" % (date_jour.day, date_jour.month, date_jour.year)
    # Cree une liste vide pour acceuillir les fichiers atbudget 
    good_file = list()
    logging.basicConfig(filename='atbudget.log',level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    subprocess.Popen("mkdir %s%s" % (a, name_dir), shell=True)
    logging.info('Creation du dossier %s' %(name_dir))
    time.sleep(10)
    at_budget_folder = os.path.join(a, name_dir)
    for (root, dirs, files) in os.walk(a):
        file_date = os.path.getmtime(root)
        for fi in files:
            full_file = os.path.join(root, fi)
            date_created = os.path.getctime(full_file)
            date_format = datetime.datetime.fromtimestamp(date_created).date()
            date_today = datetime.date.today()
            if date_format == date_today:
                if fi.startswith('lass'):
                    at_budget_file = os.path.join(root, fi)
                    good_file.append(at_budget_file)
    for file in good_file:
        shutil.move(file, at_budget_folder)
    time.sleep(10)
    shutil.make_archive(at_budget_folder, 'zip',at_budget_folder)
    time.sleep(10)
    logging.info('Compression du dossier %s' %(name_dir))
    sender = 'mail_sender@mailsender.com'
    password_sender = os.environ.get('PASS')
    subject = name_dir
    body = "Bonjour,\n Veuillez trouver ci-joint les fichiers atbudget du jour \n Cordialement."
    mail_list = [
        'recipent1@tester1.net',
        'recipent2@tester2.com',
    ]
    for mail in mail_list:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ''.join(mail)
        msg['Subject'] = subject
        text = msg.as_string()
        msg.attach(MIMEText(body, 'plain'))
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(at_budget_folder +'.zip', "rb").read())
        encoders.encode_base64(part)
        time.sleep(20)
        part.add_header('Content-Disposition', "attachment; filename=%s.zip" %(name_dir))
        msg.attach(part)
        try:
            server = smtplib.SMTP('xxxxx.gmail.com', 587)
            server.starttls()
            server.login(sender, password_sender)
            text = msg.as_string()
            server.sendmail(sender, mail, text)
            logging.info('Dossier %s envoye a %s' %(name_dir, mail))
            server.quit()
        except:
            pass
    logging.critical('Probleme de connexion au serveur SMTP')

at_butget_jour()