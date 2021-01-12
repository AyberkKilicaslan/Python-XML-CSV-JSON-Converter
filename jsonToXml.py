import csv
import json
import xml.etree.ElementTree as etree
import xml.dom.minidom

def jsontoxml(input_file,output_file):
    ##parsing json file as a input file
    jsonFile = open(input_file,encoding="utf-8")

    json_dict = json.load(jsonFile)
    backUpName = "differentName" ##temp string for name control in order to print comma
    dataRoot = etree.Element("departments")
    ##searching in dictionary 
    for temp in json_dict:
        for subitem in temp["item"]:
            for items in subitem["department"]:
                uniName = temp["university name"]

                if uniName != backUpName:
                    itemUni = etree.SubElement(dataRoot, 'university', name=temp["university name"], uType=temp["uType"])
                    
                ##main part to create xml file like csvToXml function
                item = etree.SubElement(itemUni, 'item', id=items["id"], faculty=subitem["faculty"])

                name = etree.SubElement(item, 'name', lang=items["lang"], second=items["second"])

                name.text = items["name"]

                period = etree.SubElement(item, 'period').text = items["period"]

                quota = etree.SubElement(item, 'quota', spec=items["spec"]).text = items["quota"]

                field = etree.SubElement(item, 'field').text = items["field"]
                
                last_min_score = etree.SubElement(item, 'last_min_score', order=items["last_min_order"]).text = items["last_min_score"]

                grant = etree.SubElement(item, 'grant')
                if items["grant"] != '':
                    grant.text = items["grant"]

                backUpName = temp["university name"]
                ##change the temp value for next line control

    mydata = etree.tostring(dataRoot, encoding='utf-8')
    nice = xml.dom.minidom.parseString(mydata) ##pretty print part
    niceu = nice.toprettyxml(encoding="utf-8")
    myfile = open(output_file, "wb")
    myfile.write(niceu)
    myfile.close()




