import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
prices = []
for el in elements:
    for child in el.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Value':
                prices.append(child.firstChild.data)

ob_znach = 0
for i in prices:
    ob_znach += float(i.replace(',', '.'))

srednee_znach = ob_znach / len(prices)
print('Средний показатель Value:', srednee_znach)

xml_file.close()
