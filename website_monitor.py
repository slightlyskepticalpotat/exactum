import logging
import queue
import smtplib
import sys
import threading
import time
import tkinter
import tkinter.messagebox

import browser_cookie3
import requests
import yaml


def message_box(message):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo(message[0], message[1])
    root.destroy()


def track_website(job, url, delay, notify, email):
    '''Tracks a website and displays a desktop notification.'''
    last = ""
    while True:
        logging.info(f"{job} checked")
        response = requests.get(url, allow_redirects=True, cookies=yum)
        if not response.status_code == 200:
            logging.info(f"{job} unreachable")
            if notify:
                messages.put(
                    ("Website Unreachable", f"{job} is unreachable at {time.strftime('%X %x %Z')}."))
            if email:
                server.sendmail(email_settings["from_address"], email_settings["to_address"],
                                f"\n{job} is unreachable at {time.strftime('%X %x %Z')}.")
        elif response.text != last and last:
            logging.info(f"{job} changed")
            if notify:
                messages.put(
                    ("Website Changed", f"{job} has changed at {time.strftime('%X %x %Z')}."))
            if email:
                server.sendmail(email_settings["from_address"], email_settings["to_address"],
                                f"\n{job} has changed at {time.strftime('%X %x %Z')}.")
            last = response.text
        time.sleep(delay)


with open("config.yml") as config_file:
    config = yaml.full_load(config_file)
if not config:
    message_box(("Notification", "Configuration file missing; exiting"))
    sys.exit()
try:
    with open("email.yml") as email:
        email_settings = yaml.full_load(email)
except:
    email_settings = {}
if email_settings:
    try:
        server = smtplib.SMTP(email_settings["server"], email_settings["port"])
        server.starttls()
        server.login(email_settings["from_address"],
                     email_settings["password"])
    except:
        message_box(("Notification", "Email misconfigured; exiting"))
yum = browser_cookie3.load()
if not yum:
    message_box(
        ("Notification", "No browser cookies detected; logins will not work"))
logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                    datefmt="%H:%M:%S", filename="website_monitor.log")

messages = queue.Queue(maxsize=0)
for job in config:
    logging.info(f"Starting monitoring job: {config[job]}")
    threading.Thread(target=track_website, args=(job,
                                                 config[job]["url"], config[job]["delay"], config[job]["notify"], config[job]["email"])).start()
while True:
    while messages:
        latest = messages.get()
        message_box(latest)
    time.sleep(10)
