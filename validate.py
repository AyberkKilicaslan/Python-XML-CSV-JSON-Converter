from lxml import etree
from io import StringIO

def validation(input_file,xsd_file):
    doc = etree.parse(input_file)  ##parsing xml input file
    root = doc.getroot()        ##reaching the root 
    xmlschema_doc = etree.parse(xsd_file)  ##parsing xsd file 
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.XML(etree.tostring(root))
    validation_result = xmlschema.validate(doc)     ##validate part in order to xsd schema

    #print(validation_result)
    if validation_result == True:
        print("Validation succesful")
    else:
        print("Validation failed")    
    
    xmlschema.assert_(doc)