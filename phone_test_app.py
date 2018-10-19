# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:27:18 2018

@author: user
"""
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
import datetime
import time


class SingleButtonMode(BoxLayout):
    pass

class LoggingButton(Button):
    
    def log_press(self):
        print("logging")
        with open("{}.txt".format(PhoneTestApp.filename),"a") as f:
            f.write("{}\t{}\t{}\t{}\n".format(self.name,"press",time.time(),
                    datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))
    def log_release(self):
        print("logging")
        with open("{}.txt".format(PhoneTestApp.filename),"a") as f:
            f.write("{}\t{}\t{}\t{}\n".format(self.name,"release",time.time(),
                    datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))

class StartStopButton(Button):
    
    def start_logging(self):
        self.initializeRecord()
    

    def initializeRecord(self):
        PhoneTestApp.filename = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.text = "Logging in {}.\n Click to log in a new file.".format(PhoneTestApp.filename)
        print("Starts logging. File name {}".format(PhoneTestApp.filename))
        f = open("{}.txt".format(PhoneTestApp.filename),"w+")
        f.close()
           

class PhoneTestApp(App):
    
    filename = ""
    
    def build(self):
        return SingleButtonMode()


if __name__ == '__main__':
    PhoneTestApp().run()
