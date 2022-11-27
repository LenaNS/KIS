import generator_mod
import xml.etree.ElementTree as et
import json

if __name__ == "__main__":   
    fio = generator_mod.Generator_name()
    list_fio, list_oms = fio.get_fio()

    def form_xml(list_fio, list_oms):
        fio1 = et.Element('fio')
        items_fio = et.SubElement(fio1, 'items_fio')
        for n, s in zip(list_fio, list_oms):
            print(n)
            surname = et.SubElement(items_fio,'surname')
            name = et.SubElement(items_fio,'name')
            oms = et.SubElement(items_fio, "oms")
            patronymic = et.SubElement(items_fio,'patronymic')
            surname.set('name','surname') 
            name.set('name','name')
            patronymic.set('name','patronymic')
            oms.set('oms','oms')


            list_name = n.split()
            surname.text = list_name[0]
            name.text = list_name[1]
            patronymic.text = list_name[2]
            oms.text = s

            mydata =et.tostring(fio1, encoding='unicode')
            myfile = open("fio_2.xml", "w", encoding="utf-8")
            myfile.write(mydata + "\n")
    form_xml(list_fio, list_oms)

def form_json(list_fio, list_oms):
    js = []
    for n, s in zip(list_fio, list_oms):
        list_name = n.split()
        surname = list_name[0]
        name = list_name[1]
        patronymic = list_name[2]
        oms = s

        to_json = {'surname': str(surname), 'name': name, 'patronymic': patronymic, 'oms': oms}
        js.append(to_json)

        myfile = open('fio_2.json', 'w', encoding="utf-8") 
        myfile.write(json.dumps(js, indent=2, ensure_ascii=False))

form_json(list_fio, list_oms)