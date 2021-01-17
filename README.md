# exactum

---

This configurable python script allows you to monitor any webpage for changes. It was created during Hack the North 2020 by AlanL2, Maillew, and I.

Before using this, you need to create a configuration file named `config.yml`. For each site you want to monitor, add an an entry to the file with the following format. The first line is the name of the monitor, the delay between checks is in seconds, and a pop-up dialog will be shown if you set notify to true.
```yaml
monitor-google:
    url: https://google.ca
    delay: 60
    notify: True
    email: False
```
If you set email to true, you will need to specify your settings for a SMTP server in a file named `email.yml`. When a website changes, it will notify you via email. Here is the format:
```yaml
server: smtp.gmail.com
port: 587
from_address: fromemail@exactum.com
to_address: toemail@exactum.com
password: exactummutcaxe
```
If you are using the .py file, install Python 3 and the dependencies in README.md.
