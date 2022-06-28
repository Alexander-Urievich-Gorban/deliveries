from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Sum
from celery import shared_task
from conf.celery import app
from services.order_db import read_exel, update_order


@shared_task(bind=True)
def run(self):
    while True:
        result = read_exel('1QxBtlWpCsdrtNceT33nm7eef8NN-V2gNRpKP5DNxOek', 'A1:D51')
        for res in result:
            if res[0] == '№':
                continue
            update_order(res[0], res[1], res[2], res[3])


