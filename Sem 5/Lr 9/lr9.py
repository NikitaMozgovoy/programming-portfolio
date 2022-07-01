import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date, timedelta
import requests
from bs4 import BeautifulSoup


def get_currencies(currencies_ids_lst=None):
    """
    Функция записывает в словарь название и значение запрошенных валют в рублях
    """
    if currencies_ids_lst is None:
        currencies_ids_lst = [
            'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
            'R01625', 'R01670', 'R01700J', 'R01710A'
        ]
    cur_res_str = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
    result={}
    soup = BeautifulSoup(cur_res_str, 'html.parser')
    valutes = soup.find_all("valute")
    for _v in valutes:
        valute_id = _v['id']
            
        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = _v.find('value').string
            valute_cur_name = _v.find('name').string
            result[valute_cur_name] = valute_cur_val

    return result




def get_currencies_year(currencie_id='R01239'):
    """
    Функция записывает в словарь название и значение запрошенной валюты в рублях за год
    """
    today = datetime.today()
    date = today - timedelta(days=365)
    result={}
    valute_name="Евро"
    while date !=today:

        day = str(date.day)
        month = str(date.month)

        if len(str(date.day)) == 1:
            day = '0' + str(date.day)
        
        if len(str(date.month)) == 1:
            month = '0' + str(date.month)

        req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params = {'date_req':day + '/' + month + '/' + str(date.year)}).text

        soup = BeautifulSoup(req, 'html.parser')
        valutes = soup.find_all("valute")
        for _v in valutes:
            valute_id = _v['id']
                
            if str(valute_id) == currencie_id:
                valute_val = float('.'.join(_v.find('value').string.split(',')))
                result[date.strftime("%d/%m/%Y")] = valute_val
        date = date + timedelta(days = 1)
    res = {valute_name:result}
    return res

#Отрисовка диграммы на 10 валют
cur_vals = get_currencies()
objects = cur_vals.keys()
y_pos = np.arange(len(objects))
performance = [float(x.replace(',', '.')) for x in cur_vals.values()]

bars = plt.bar(y_pos, performance, color = ["orange", "purple", "darkturquoise", "firebrick", "limegreen", "red", "blue", "black", "pink", "yellow"])
plt.ylabel('Стоимость')
plt.xlabel('Валюта')
plt.title('Курс валют по отношению к рублю')
plt.legend(bars, objects)
plt.show()

#Отрисовка графика за год
year_currencies = get_currencies_year()
x=[]
y=[]
for n in list(year_currencies["Евро"].items()):
    x.append(n[0])
    y.append(n[1])
plt.plot(x,y)
plt.title("Курс евро по отношению к рублю за год")
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.yticks(y[::1])
plt.xticks(x[::1])
plt.show()