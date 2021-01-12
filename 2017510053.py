##import sys to taking arguement from command line
import sys
##import OOP based classes
import csvToXml
import csvToJson
import jsonToCsv
import jsonToXml
import xmlToCsv
import xmlToJson
import validate

##Main program if else statement to decide which operation will be used
if  len(sys.argv) < 4:
    print("You need to enter at least 3 arguement !!!")
    print("For example : 'python_file_name.py input_file.xxx output_file.xxx'")
elif len(sys.argv) > 4:   ##if user entered more than 3 arguement
    print("You entered more than 3 arguement")
else:

    ### CSV to XML Part
    if sys.argv[3] == "1":
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".xml"):
            print("CSV to XML convert is done !")
            csvToXml.csvtoxml(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions")

    ### XML to CSV Part
    elif sys.argv[3] == "2": 
        if sys.argv[1].endswith(".xml") and sys.argv[2].endswith(".csv"):  
            print("XML to CSV convert is done !")
            xmlToCsv.xmltocsv(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions")

    ### XML to JSON Part        
    elif sys.argv[3] == "3":  
        if sys.argv[1].endswith(".xml") and sys.argv[2].endswith(".json"):
            print("XML to JSON convert is done !")
            xmlToJson.xmlToJson(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions") 

    ### JSON to XML Part        
    elif sys.argv[3] == "4":
        if sys.argv[1].endswith(".json") and sys.argv[2].endswith(".xml"):
            print("JSON to XML convert is done !")
            jsonToXml.jsontoxml(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions")  

    ### CSV to JSON Part
    elif sys.argv[3] == "5":
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".json"):
            print("CSV to JSON convert is done !")
            csvToJson.csvToJson(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions")    

    ### JSON to CSV Part
    elif sys.argv[3] == "6":
        if sys.argv[1].endswith(".json") and sys.argv[2].endswith(".csv"):  
            print("JSON to CSV convert is done !")
            jsonToCsv.jsontocsv(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions")   

    ### XML Validate Part       
    elif sys.argv[3] == "7":
        if sys.argv[1].endswith(".xml") and sys.argv[2].endswith(".xsd"):  
            print("Validate XML file is done !")
            validate.validation(sys.argv[1],sys.argv[2])
        else:
            print("Invalid file extensions")    

    ## Error Part
    else:
        print("invalid function arguement")








