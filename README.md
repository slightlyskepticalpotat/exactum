# exactum

---

This configurable python script allows you to monitor any webpage for changes. It was created during Hack the North 2020 by AlanL2, Maillew, and I.

Before using this, you need to create a configuration file named `config.yml`. For each site you want to monitor, add an an entry to the file with the following format. The first line is the name of the monitor, the delay between checks is in seconds, and a pop-up dialog will be shown if you set notify to true.
```yaml
monitor-google:
    url: https://google.ca
    delay: 60
    notify: True
```
If you are using the .py file, install Python 3 and the dependencies in README.md.
