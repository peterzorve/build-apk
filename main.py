from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup 
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivymd.uix.pickers import MDDatePicker
import sqlite3 as sq  
import random 
import string
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.metrics import dp
from kivy.clock import Clock 
# from helper_function import initialize_database 
from kivymd.uix.card import MDCard 
# from kivy.app import App 
import random


class Screen_Manger(ScreenManager):
    pass 


class HomePage(Screen):
    pass


class CalculatorApp(MDApp):
    # initialize_database()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return super().build()



CalculatorApp().run() 