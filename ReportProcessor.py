import RemoteConnector

addressMap = {
    "00124b000c479e07": "f64c0932-de24-4c6b-bb13-58b9396973fc"
} 
CCId = "ac2ad2c3-252d-4fb8-a0de-e37ae5751a6b"

def raw_report_handler(ieeeAddress, occupancyState):

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
    
    
