import xml.etree.ElementTree as ET
from io import StringIO
import requests
import pandas as pd

# url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# raw = pd.read_xml(url, encoding='cp1251')
#
# # print(pd.read_xml(url, encoding='cp1251'))
# # print(pd.DataFrame(raw, columns=['CharCode', 'Name', 'Value']))
# df_new = raw[raw['Name'] == 'Белорусский рубль']
# print(pd.DataFrame(df_new, columns=['CharCode', 'Name', 'Value']))

def get_currency_rate(name_cur:str):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    raw = pd.read_xml(url, encoding='cp1251')

    # print(pd.read_xml(url, encoding='cp1251'))
    # print(pd.DataFrame(raw, columns=['CharCode', 'Name', 'Value']))
    df_new = raw[raw['Name'] == name_cur]
    return (pd.DataFrame(df_new, columns=['CharCode', 'Name', 'Value']))

print(get_currency_rate('Фунт стерлингов Соединенного королевства'))


