from bs4 import BeautifulSoup
import requests
from urllib import parse
import xml.etree.ElementTree as ET



def query(method: str, **kwargs):
    """
    Отправляю запрос к ISS MOEX
    :param method:
    :param kwargs:
    :return:
    """
    try:
        url = "https://iss.moex.com/iss/%s.xml" % method
        if kwargs: url += "?" + parse.urlencode(kwargs)
        response = requests.get(url)
        # tree = ET.parse(response.text)
        # root = tree.getroot()
        # with open('data.xml', 'a', encoding='utf-8') as f:
        #     f.write(response.text)
        # print(response.text)
        # response.encoding = 'utf-8'
        return response

    except Exception as e:
        print("query error %s" % str(e))
        return None




def main():

    # Дивиденды по акциям
    # ** описания нет
    secid = 'LSRG'
    method = "securities/%s/dividends" % secid
    div_info = query(method)
    soup = BeautifulSoup(div_info.text, 'xml')
    id = soup.find_all('secid')
    date = soup.find_all('registryclosedate')
    value = soup.find_all('value')
    currency = soup.find_all('currencyid')
    print('-'.center(35, '-'))
    print('|' + 'Id'.center(15) + '|' + ' Date ' + '|' + 'Subject'.center(11) + '|')
    for i in range(0, len(id)):
        print('-'.center(35, '-'))
        print(
            f'|{id[i].text.center(15)}|{date[i].text.center(5)}|{value[i].text.center(11)}|')
    print('-'.center(35, '-'))




if __name__ == '__main__':
    main()
