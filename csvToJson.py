import csv
import json

def csvToJson(input_file,output_file):
    ###reading csv file part
    csv_file = csv.reader(open(input_file, 'r',encoding="utf-8"), delimiter=';')
    ##json will write in this file
    jsonfile = open(output_file, 'w',encoding="utf-8")
    
    ##deutemp value for control university names 
    deutemp = "DOKUZ EYLÜL ÜNİVERSİTESİ"
    jsonfile.write('[\n')
    ##two different temp strings for printing comma(,)
    temp = "temp"
    differentTemp = "different"

    ##skip the first line because we dont need in json file
    next(csv_file)
    for row in csv_file:
        ##some replace parts for json file
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
        
        if differentTemp != "different" :
            if row[1] == deutemp :    
                jsonfile.write('                        },\n')
            else:
                jsonfile.write('                        }\n')  

        differentTemp = "anotherDifferent"
          
        ##if the next line's university name is different then close the tags!!!! 
        if row[1] != deutemp :
            jsonfile.write('                    ]\n')
            jsonfile.write('                }\n')
            jsonfile.write('        ]\n')
            jsonfile.write('    },\n')
        
        ###print university name only once for same university
        if row[1] != temp:
            jsonfile.write('    {\n')
            jsonfile.write('        \"university name\" : ')
            jsonfile.write(json.dumps(row[1], indent=4, ensure_ascii=False))
            jsonfile.write(',\n')

            jsonfile.write('        \"uType\" : ')
            jsonfile.write(json.dumps(row[0], indent=4, ensure_ascii=False))
            jsonfile.write(',\n')

            jsonfile.write('        \"item\" : \n')
            jsonfile.write('        [\n                {\n')

            jsonfile.write('                    \"faculty\" : ')
            jsonfile.write(json.dumps(row[2], indent=4, ensure_ascii=False))
            jsonfile.write(',\n')

            jsonfile.write('                    \"department\" : \n')
            jsonfile.write('                    [\n')
            temp = row[1]
        
        ####Main loop print part with all attributes
        jsonfile.write('                        {\n')
        jsonfile.write('                            \"id\" : ')
        jsonfile.write(json.dumps(row[3], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"name\" : ')
        jsonfile.write(json.dumps(row[4], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"lang\" : ')
        jsonfile.write(json.dumps(row[5], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"second\" : ')
        jsonfile.write(json.dumps(row[6], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"period\" : ')
        jsonfile.write(json.dumps(row[8], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"spec\" : ')
        jsonfile.write(json.dumps(row[11], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"quota\" : ')
        jsonfile.write(json.dumps(row[10], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"field\" : ')
        jsonfile.write(json.dumps(row[9], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"last_min_score\" : ')
        jsonfile.write(json.dumps(row[13], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"last_min_order\" : ')
        jsonfile.write(json.dumps(row[12], indent=4, ensure_ascii=False))
        jsonfile.write(',\n')

        jsonfile.write('                            \"grant\" : ')
        jsonfile.write(json.dumps(row[7], indent=4, ensure_ascii=False))
        jsonfile.write('\n')
        
        ##reassign the temp values for next control parts
        temp = row[1]
        deutemp = row[1]


    ##closing the json file 
    jsonfile.write('                        }\n')
    jsonfile.write('                    ]\n')
    jsonfile.write('                }\n')
    jsonfile.write('        ]\n')
    jsonfile.write('    }\n')
    jsonfile.write(']')

##call the csvToJson function
   