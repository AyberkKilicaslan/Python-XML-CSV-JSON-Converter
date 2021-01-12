import xml.etree.ElementTree as etree
import csv
import xml.dom.minidom

def csvtoxml(input_file,output_file):
    ##CSV file reading with delimiter "";""
    f = open(input_file,'r',encoding="utf-8")
    csv_f = csv.reader(f, delimiter=";")

    next(f)  ##skip the first line to not include in xml scheme
    backUpName = "differentName" ##some string for university name control
    dataRoot = etree.Element("departments")  ##root element assign
    for row in csv_f:
        ##replace words in csv file in order to wanted xml file format
        if row[6] == '':
            row[6] = "no"
        else:
            row[6] = 'yes'
        if row[5] == '':
            row[5] = "tr"
        else:
            row[5] = "en"
        if row[13] == '':
            row[13] = '0'
    

        if row[12] == '' or row[12] == '-':
            row[12] = '0'
        if row[11] == '':
            row[11] = '0'
        uniName = row[1] ##univeristy name

        ##only add university name once
        if uniName != backUpName:
            itemUni = etree.SubElement(dataRoot, 'university', name=row[1], uType=row[0])

        ##assigning subelement with their attributes if they have
        item = etree.SubElement(itemUni, 'item', id=row[3], faculty=row[2])

        name = etree.SubElement(item, 'name', lang=row[5], second=row[6])

        name.text = row[4]

        period = etree.SubElement(item, 'period').text = row[8]

        quota = etree.SubElement(item, 'quota', spec=row[11]).text = row[10]

        field = etree.SubElement(item, 'field').text = row[9]
        
        last_min_score = etree.SubElement(item, 'last_min_score', order=row[12]).text = row[13]

        grant = etree.SubElement(item, 'grant')
        if row[7] != '':
            grant.text = row[7]
        
        ##change the temp value for next line control
        backUpName = row[1]

    ##writing to the file xml type
    mydata = etree.tostring(dataRoot, encoding='utf-8')
    nice = xml.dom.minidom.parseString(mydata) ##pretty print part
    niceu = nice.toprettyxml(encoding="utf-8")
    myfile = open(output_file, "wb")
    myfile.write(niceu)  ##write file as a form pretty xml
    myfile.close()



