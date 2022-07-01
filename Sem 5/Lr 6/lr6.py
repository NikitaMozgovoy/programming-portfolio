"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения отправки избыточных запросов к серверу ЦБ РФ (запретить вызов функции get_currencies более 1 раза в секунду). Оформить решение в виде корректно работающего приложения, реализовать тестирование и опубликовать его в портфолио.

Страница документации: https://cbr.ru/development/
"""

# http://www.cbr.ru/scripts/XML_daily.asp
import requests
from bs4 import BeautifulSoup


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class CurrenciesList(metaclass=MetaSingleton):

    def get_currencies(self, currencies_ids_lst=None):
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

                result[valute_id] = (valute_cur_val, valute_cur_name)
        return result


my_cur_list = CurrenciesList()


my_cur_list2 = CurrenciesList()
res = my_cur_list2.get_currencies(["R01090B", "R01720", "R01565"])
print(res)


