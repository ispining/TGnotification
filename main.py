from pyrogram import Client
import subprocess, threading, time


class bot:
    def __init__(self, app_name=None, show_time=False):
        self.app = Client("my_account", 
                    api_id=5914799,
                    api_hash="1414ee09495a39d6d8a78680364679b5",
                    )
        self.show_time = show_time
        self.app_name = app_name

    def send_msg(self, text):
        with self.app as app:
            if self.app_name != None:
                text = "device: " + self.app_name + " \n" + text
            app.send_message("me", text)
    def send_buttery_msg(self):
        trmx = termux()
        self.send_msg(f"~ Battery = {str(trmx.battery())}%")
    def send_low_battery_msg(self):
        self.send_msg("Low battery!")
    def start_battery_thread(self):
            self.num = 0
            while self.num < 3:
                if termux().battery() < 20:
                    self.send_low_battery_msg()
                    self.num = self.num + 1
                time.sleep(60)
            self.num = 0


class termux:
    def __init__(self):
        self.command = "termux-"
    def battery(self):
        result = subprocess.getoutput(self.command + 
        "battery-status")
        return int(result.splitlines()[2].split(": ")[1][:-1])


b = bot(app_name="Personal Phone")
b.start_battery_thread()




