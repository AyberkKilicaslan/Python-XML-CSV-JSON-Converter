import xml.etree.ElementTree as ET
import csv
def xmltocsv(input_file,output_file):
    ##parsing the xml file with ET
    xml_Parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input_file,parser=xml_Parser)
    root = tree.getroot()

    # open a file for writing
    csv_data = open(output_file, 'w', encoding="utf-8")

    ##variables for easy print will be used in for loop
    second = ''
    grant = ''
    period = ''
    spec = ''
    lastScore = ''
    field = ''
    quota_text = ''

    ##writing the first line of the csv manually
    csv_data.write("ÜNİVERSİTE_TÜRÜ;ÜNİVERSİTE;FAKÜLTE;PROGRAM_KODU;PROGRAM;DİL;ÖĞRENİM_TÜRÜ;BURS;ÖĞRENİM_SÜRESİ;PUAN_TÜRÜ;KONTENJAN;OKUL_BİRİNCİSİ_KONTENJANI;GEÇEN_YIL_MİN_SIRALAMA;GEÇEN_YIL_MİN_PUAN\n")

    ##reach the "university" members
    for member in root.findall('university'):
        
        for submemer in member:
            csv_data.write(member.get("uType") +";")
            csv_data.write(member.get("name")+";")
            csv_data.write(submemer.get("faculty")+";")
            csv_data.write(submemer.get("id")+";")
            
            for submember in submemer:
                ###department has to be here
                if submember.tag == "name":
                    csv_data.write(submember.text+";")

                if submember.tag == "name":
                    if submember.get("lang") == "en":   ##change the strings for expected csv file format
                        csv_data.write("İngilizce;") 
                    else :
                        csv_data.write(";")

                ##replace the xml attributes to the expected original csv file format
                ##reaching the whole element tag's attributes with cheking if else for each subelement
                if submember.tag =="grant":
                    if submember.text is None:
                        grant = ';'  
                    else:
                        grant = submember.text+";" 

                if submember.tag == "period":
                    if submember.get("period") != None:
                        period = submember.get("period")+";"  

                if submember.tag == "name":
                    if submember.get("second") == "no":
                        second = ";"
                    else :
                        second = "İkinci Öğretim;"

                if submember.tag =="field":
                        if submember.text != None:
                            field = submember.text+";"
                                        
                if submember.tag =="period":
                    period = submember.text+";" 
                    
                if submember.tag == "quota":
                    spec = submember.get("spec")+";"      
                
                if submember.tag == "quota":
                    quota_text = submember.text+";" 

                if submember.tag =="last_min_score":
                    if(submember.get("order") != None):
                        if(submember.get("order") == '0'):
                            lastScore = ";"
                        else:
                            lastScore = submember.get("order")+";" + submember.text

            ##easy print part with variables which we included before              
            csv_data.write(second + grant +  period + field + quota_text + spec + lastScore)
            csv_data.write("\n")  
       


                     

           
    