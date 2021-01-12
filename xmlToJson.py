import csv
import json
import xml.etree.ElementTree as ET

def xmlToJson(input_file,output_file):
    ###main variables
    language=''
    second = ''
    grant = ''
    period = ''
    spec = ''
    order = ''
    lastScore = ''
    field = ''
    quota_text = ''
    nameTemp = ""
##parsing the xml file with ET
    xml_Parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input_file,parser=xml_Parser)
    root = tree.getroot()
    ##temp string for checking comma error whole lines
    deutemp = "DOKUZ EYLÜL ÜNİVERSİTESİ"
    temp = "temp"
    lineCount = 1
    # open a file for writing
    jsonfile = open(output_file, 'w',encoding="utf-8")
    jsonfile.write('[\n')
    for member in root.findall('university'):  ## main for loop
        ##check if the next line's university name
        if member.get("name") != deutemp :
            jsonfile.write('                    ]\n')
            jsonfile.write('                }\n')
            jsonfile.write('        ]\n')
            jsonfile.write('    },\n')
        
        jsonfile.write('    {\n')
        jsonfile.write('        \"university name\" : ')
        jsonfile.write(json.dumps(member.get("name"), indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('        \"uType\" : ')
        jsonfile.write(json.dumps(member.get("uType"), indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('        \"item\" : \n')
        jsonfile.write('        [\n                {\n')

        
        ##sub for reaching submember 
        for submember in member:

            if member.get("name") != temp:
                jsonfile.write('                    \"faculty\" : ')
                jsonfile.write(json.dumps(submember.get("faculty"), indent=4, ensure_ascii=False))
                jsonfile.write(',\n')

                jsonfile.write('                    \"department\" : \n')
                jsonfile.write('                    [\n')
            
            jsonfile.write('                        {\n')
            jsonfile.write('                            \"id\" : ')
            jsonfile.write(json.dumps(submember.get("id"), indent=4, ensure_ascii=False))
            jsonfile.write(',\n')

            
            temp = member.get("name")
            ##reaching sub items and attributes and hold them temp values for each
            for items in submember:
                if items.tag == "name":
                    nameTemp = items.text
                    language = items.get("lang")
                    second = items.get("second")
                if items.tag =="period":
                    period = items.text
                if items.tag == "quota":
                    spec = items.get("spec")
                    quota_text = items.text
                if items.tag == "field":
                    field = items.text
                if items.tag == "last_min_score":
                    lastScore = items.text
                    order = items.get("order")    
                if items.tag =="grant":
                    if items.text == None:
                        grant = ""
                    else:
                        grant = items.text    
            ##manually write json format
            jsonfile.write('                            \"name\" : ')
            jsonfile.write(json.dumps(nameTemp, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## Language
            jsonfile.write('                            \"lang\" : ')
            jsonfile.write(json.dumps(language, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## second
            jsonfile.write('                            \"second\" : ')
            jsonfile.write(json.dumps(second, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## period
            jsonfile.write('                            \"period\" : ')
            jsonfile.write(json.dumps(period, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## Spec
            jsonfile.write('                            \"spec\" : ')
            jsonfile.write(json.dumps(spec, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## Quota
            jsonfile.write('                            \"quota\" : ')
            jsonfile.write(json.dumps(quota_text, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## Field
            jsonfile.write('                            \"field\" : ')
            jsonfile.write(json.dumps(field, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## Last minimum score
            jsonfile.write('                            \"last_min_score\" : ')
            jsonfile.write(json.dumps(lastScore, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## Last order
            jsonfile.write('                            \"last_min_order\" : ')
            jsonfile.write(json.dumps(order, indent=4, ensure_ascii=False))
            jsonfile.write(',\n')
            ## and finally Grant
            jsonfile.write('                            \"grant\" : ')
            jsonfile.write(json.dumps(grant, indent=4, ensure_ascii=False))
            jsonfile.write('\n')

            #comma correction in the end of the same university 
            if lineCount == 13 or lineCount ==22 or lineCount ==50 or lineCount ==78 or lineCount ==88 or lineCount ==92 or lineCount ==97 or lineCount ==105:
                jsonfile.write('                        }\n')
            else:
                jsonfile.write('                        },\n')  

            lineCount = lineCount+1
            temp = member.get("name")
            deutemp = member.get("name")

    #closing the main json file
    jsonfile.write('                    ]\n')
    jsonfile.write('                }\n')
    jsonfile.write('        ]\n')
    jsonfile.write('    }\n')
    jsonfile.write(']')

##call the csvToJson function
#xmlToJson()