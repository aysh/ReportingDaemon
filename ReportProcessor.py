import RemoteConnector

addressMapFile = "addr-map.csv"
addressMap = {
} 
CCId = "ac2ad2c3-252d-4fb8-a0de-e37ae5751a6b"

def get_data_from_csv_line(csvLine):
    csvLine.replace('\n', '')
    csvLine.replace('\r', '')
    lowerCaseCsvLine = csvLine.lower()
    valuesArray = lowerCaseCsvLine.split(',')
    address, uuid = valuesArray[0].strip(), valuesArray[1].strip()
    return address, uuid

def check_validity(address, uuid):
    if len(address)==16 and len(uuid)==36:
        return True
    else:
        return False

def load_address_sid_map(filename):
    fObj = open(filename, 'r')
    for line in fObj:
        print line
        address, uuid = get_data_from_csv_line(line)
        print address, uuid
        if check_validity(address, uuid):
	    addressMap[address] = uuid
        else:
            print("Invalid entry")
    print addressMap

def raw_report_handler(ieeeAddress, occupancyState):

    if len(addressMap)==0:
        load_address_sid_map(addressMapFile)
    print "Processing report"
    strAddress = "%016x" % ieeeAddress
    print strAddress
    if strAddress in addressMap:
        SensorId = addressMap[strAddress]
        if occupancyState > 0:
            occState = True
        else:
            occState = False
        RemoteConnector.threaded_send_report(CCId, SensorId, occState)
    else:
        print "Invalid Sensor address!!"
    
    
