import datetime
import os
from typing import re
import asyncio
from googleapiclient.discovery import build
import requests
from google.oauth2 import service_account

from orders.models import Order


def read_exel(sample_spreadsheet_id, sample_range_name):
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    base_dir = os.path.dirname(os.path.abspath(__file__))
    service_account_file = os.path.join(base_dir, 'credentials.json')
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sample_spreadsheet_id, range=sample_range_name).execute()
    return result['values']


def get_course(valute='USD'):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return int(data['Valute'][valute]['Value'])


def update_order(short_number, number, dol_price, delivery_time):
    try:
        Order.objects.create(
            id=short_number,
            number=number,
            dol_price=dol_price,
            rub_price=(get_course('USD') * int(dol_price)),
            delivery_time=str(delivery_time)
        )
    except:
        Order.objects.filter(id=short_number).update(
            number=number,
            dol_price=dol_price,
            rub_price=(get_course('USD') * int(dol_price)),
            delivery_time=str(delivery_time)
        )


