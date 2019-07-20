import os
import json

#create json file
command = "sensors -j | sed -e 's/-//g' > sed -e 's/ //g' > sed -e 's/_//g' > test.json"
os.system(command)

#get temperature
with open("/home/dianas/Documents/sensor_temperature/test.json", 'r') as open_json:
    json_store = json.load(open_json)
temperature = json_store["coretempisa0000"]["Packageid0"]["temp1input"]

#set critical temperature and notification command
critical_temperature = 94
notification_command = "notify-send -i /home/dianas/Pictures/thermometer.png WARNING 'CPU temperature is '"
get_process_with_highest_cpu_usage = "ps -eo pid,%cpu | sort -nrk 3,3 | sed -n '2p' > test_ps.txt"

limit_process_command = ""

if temperature <= critical_temperature:
    notification_command += str (temperature)
    os.system(notification_command)
    os.system(get_process_with_highest_cpu_usage)
    #file_process = open("test_ps.txt","r")
    #process_kill = file_process.read()
#    print (process_kill)
    with open('test_ps.txt','r') as f:
        for line in f:
            for word in line.split():
                print(word)

