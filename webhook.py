from flask import Flask, request
import RPi.GPIO as GPIO
import logging
import subprocess
import json
import time
from datetime import datetime
import threading
from check_db import checkTime
import fritz_script

logging.basicConfig(filename='webhook.log',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

webhook_status = False  # WebHook-Status
schedule_active = False  # Bewegungssensor-Status


app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
    global webhook_status
    alarm_status = request.args.get('Alarm')  # Liest den 'Alarm'-Parameter aus der URL
    if alarm_status is not None:
        logging.info(f"Webhook received with Alarm: {alarm_status}")
        
        if alarm_status:
            webhook_status = True
        else:
            webhook_status = False            
        
        update_monitor()
        fritz()
        return f"Alarm status received: {alarm_status}", 200
        
    else:
        return "No Alarm status provided", 400  # Rückmeldung, falls der Parameter fehlt

def monitorTime():
    
    global schedule_active
    #current_time = datetime.now()
    
    #with open('/home/amweb/dutyTime.json') as f:
    #    times = json.load(f)
    #schedule = times['times']
    #schedule_active = any(is_time_in_range(entry["on"], entry["off"], current_time) for entry in schedule)
    schedule_active = checkTime()
    update_monitor()
        
def is_time_in_range(start, end, current_time):
    """Überprüft, ob die aktuelle Zeit innerhalb eines Bereichs liegt."""
    fmt = "%d.%m.%Y %H:%M"
    start_time = datetime.strptime(start, fmt)
    end_time = datetime.strptime(end, fmt)
    return start_time <= current_time <= end_time

def update_monitor():
    
    global webhook_status, schedule_active
    
    if webhook_status or schedule_active:
        GPIO.output(23, GPIO.HIGH)
        subprocess.Popen(['bash','-c','. /home/pi/.divera_commands.sh; hdmi_onoff on'])
        
        
    else:
        GPIO.output(23, GPIO.LOW)
        subprocess.Popen(['bash','-c','. /home/pi/.divera_commands.sh; hdmi_onoff off'])
        
        


def schedule_check():
    """Läuft in einem separaten Thread und prüft den Zeitplan."""
    while True:
        monitorTime()
        time.sleep(30)  # Überprüfe den Zeitplan jede Minute


def fritz():
    
    global webhook_status
    
    if webhook_status:
        fritz_script.fritz_dect_on()
    else:
        fritz_script.fritz_dect_off()



if __name__ == '__main__':
    
    threading.Thread(target=schedule_check, daemon=True).start()
    app.run(host='127.0.0.1', port=4000)  # Webserver auf localhost starten
    monitorTime()
    
    
    #http://ygctwynnrkmddbluqawvkw.webrelay.io/?Alarm=true