import pandas as pd
import json
import requests
from urllib import parse

pd.set_option("display.max_columns", 15)


def query(method: str, **kwargs):
    """
    Отправляю запрос к ISS MOEX
    :param method:
    :param kwargs:
    :return:
    """
    try:
        url = "https://iss.moex.com/iss/%s.json" % method
        if kwargs: url += "?" + parse.urlencode(kwargs)
        response = requests.get(url)
        response.encoding = 'utf-8'
        response_dict = response.json()
        return response_dict

    except Exception as e:
        print("query error %s" % str(e))
        return None


def flatten(response_dict: dict, blockname: str):
    """
    Собираю двумерный массив (словарь)
    :param response_dict:
    :param blockname:
    :return:
    """

    return [{k: r[i] for i, k in enumerate(response_dict[blockname]
                                           ['columns'])} for r in response_dict[blockname]
                                            ['data']]


def main():
    # Список бумаг торгуемых на московской бирже
    # r_list = query("securities", group_by="type", group_by_filter="common_share", limit=10)
    # flat = flatten(r_list, 'securities')
    # print(pd.DataFrame(flat, columns=['secid', 'shortname']))
    # Спецификация инструмента
    # https://iss.moex.com/iss/reference/13
    # secid = 'SBER'
    # method = "securities/%s" % secid
    # j = query(method)
    # flat = flatten(j, 'description')

    # Купоны по облигациям
    # ** описания нет
    # secid = 'RU000A102QJ7'
    # method = "securities/%s/bondization" % secid
    # j = query(method)
    # f = flatten(j, 'coupons')

    # Дивиденды по акциям
    # ** описания нет
    # secid = 'LSRG'
    # method = "securities/%s/dividends" % secid
    method = 'statistics/engines/currency/markets/selt/rates'
    j = query(method)
    flat = flatten(j, 'cbrf')
    # print(j)

    print(pd.DataFrame(flat))
    # print(pd.DataFrame(f, columns=['secid','shortname' ,'primary_boardid', 'type']))
    # print(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
