import os
import requests

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout

# List of cities for use in spinner
from .data import CITIES

from dotenv import load_dotenv

load_dotenv()

#  get API info from .env
API_KEY = os.getenv('API_KEY')
API_URL_LIST = os.getenv('API_URL_LIST')

