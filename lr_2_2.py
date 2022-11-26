import generator_mod
import xml.etree.ElementTree as et
import json

if __name__ == "__main__":   
    fio = generator_mod.Generator_name()
    list_fio = fio.get_fio()

    def form_xml(f_i_o):
        fio1 = et.Element('fio')
        items_fio = et.SubElement(fio1, 'items_fio')
        surname = et.SubElement(items_fio,'surname')
        name = et.SubElement(items_fio,'name')
        patronymic = et.SubElement(items_fio,'patronymic')
        surname.set('name','surname') 
        name.set('name','name')
        patronymic.set('name','patronymic')

        

        surname.text = f_i_o[0]
        name.text = f_i_o[1]
        patronymic.text = f_i_o[2]

        mydata =et.tostring(fio, encoding='unicode',)
        myfile = open("fio_2.xml", "w",encoding="utf-8")
        myfile.write(mydata + "\n")

def form_json(f_i_o):
    surname = f_i_o[0]
    print(surname)
    name = f_i_o[1]
    patronymic = f_i_o[2]

    to_json = {'surname': str(surname), 'name': name, 'patronymic': patronymic}

    with open('fio2.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(to_json, indent=2, ensure_ascii=False))