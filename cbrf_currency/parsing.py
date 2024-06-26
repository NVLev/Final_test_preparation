from lxml import etree
import requests


def parseXML(xmlFile):
    """
    Parse the xml
    """
    # xml = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    with open('curdata.xml', 'rb') as file:
        xml = file.read()
    root = etree.fromstring(xml)
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)


if __name__ == "__main__":
    parseXML("curdata.xml")
