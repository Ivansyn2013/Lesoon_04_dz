import requests
from utils import currentcy_rates


currentcy_rates((input('Введи обозначение валюты:')).upper())