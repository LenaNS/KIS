import xml.etree.ElementTree as et
import json

def form_xml(f_i_o):
    fio = et.Element('fio')
    items_fio = et.SubElement(fio, 'items_fio')
    surname = et.SubElement(items_fio,'surname')
    name = et.SubElement(items_fio,'name')
    patronymic = et.SubElement(items_fio,'patronymic')
    surname.set('name','surname') 
    name.set('name','name')
    patronymic.set('name','patronymic')
    surname.text = f_i_o[0]
    name.text = f_i_o[1]
    patronymic.text = f_i_o[2]

    mydata =et.tostring(fio, encoding='unicode')
    myfile = open("fio_3.xml", "w",encoding="utf-8")
    myfile.write(mydata)

def form_json(f_i_o):
    surname = f_i_o[0]
    print(surname)
    name = f_i_o[1]
    patronymic = f_i_o[2]

    to_json = {'surname': str(surname), 'name': name, 'patronymic': patronymic}

    with open('fio3.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(to_json, indent=2, ensure_ascii=False))


f_i_o = ['Соколов', 'Иван', 'Петрович']
form_xml(f_i_o)
form_json(f_i_o)

