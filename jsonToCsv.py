import json
import csv

def jsontocsv(input_file,output_file):
    ##import input file
    jsonFile = open(input_file,encoding="utf-8")
    #load json file
    json_dict = json.load(jsonFile)
    ##open output file
    csv_data = open(output_file, 'w', encoding="utf-8")
    ##write first line manually
    csv_data.write("ÜNİVERSİTE_TÜRÜ;ÜNİVERSİTE;FAKÜLTE;PROGRAM_KODU;PROGRAM;DİL;ÖĞRENİM_TÜRÜ;BURS;ÖĞRENİM_SÜRESİ;PUAN_TÜRÜ;KONTENJAN;OKUL_BİRİNCİSİ_KONTENJANI;GEÇEN_YIL_MİN_SIRALAMA;GEÇEN_YIL_MİN_PUAN\n")
    for item in json_dict:
        for subitem in item["item"]:
            for items in subitem["department"]:
                
                ##swap and replace operations to print csv file correctly
                    # swap en to İngilizce or tr to empty
                if items["lang"] == "en":
                    items["lang"] = "İngilizce"
                else:
                    items["lang"] = ""  

                ##swap and replace ÖĞRENİM_TÜRÜ
                if items["second"] == "no":
                    items["second"] = ""
                else:
                    items["second"] = "İkinci Öğretim"  

                ##swap 0 point to the empty
                if items["last_min_order"] == "0":
                    items["last_min_order"] = ""
                    items["last_min_score"] = ""
                if items["spec"] == "0":
                    items["spec"] = ""

                ##printing to the csv file
                csv_data.write( item["uType"] + ";" +item["university name"] + ";" +subitem["faculty"] +";"+ items["id"]+ ";")
                csv_data.write(items["name"] +";")
                csv_data.write(items["lang"]+";")
                csv_data.write(items["second"]+";")
                csv_data.write(items["grant"]+";")
                csv_data.write(items["period"]+";")
                csv_data.write(items["field"]+";")
                csv_data.write(items["quota"]+";")
                csv_data.write(items["spec"]+";")
                csv_data.write(items["last_min_order"]+";")
                csv_data.write(items["last_min_score"])
                csv_data.write("\n") 
               

        
    


