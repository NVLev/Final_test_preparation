import requests
import lxml
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def get_currency_rate():
    """
:param char_code_currency: can see here - https://www.cbr.ru/scripts/XML_daily.asp
:return: float_number
"""
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    with open('curdata.xml', 'w', encoding='windows-1251') as file:
        file.write(response.text)

    # soup = BeautifulSoup(response.text, 'xml')
    # id = soup.find_all('CharCode')
    # value = soup.find_all('Value')
    # name = soup.find_all('Name')
    # for i in range(0, len(id)):
    #     if id == currency:
    #         return id, name, value
    # print('-'.center(35, '-'))
    # print('|' + 'Id'.center(15)  + 'Value'.center(11) + '|')
    # for i in range(0, len(id)):
    #     print('-'.center(35, '-'))
    #     print(
    #         f'|{id[i].text.center(15)}|{value[i].text.center(11)}|')
    # print('-'.center(35, '-'))


value = get_currency_rate()
print(value)
    # return float(ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text).
    # find('./Valute[CharCode="USD"]/Value').text.replace(',', '.'))
