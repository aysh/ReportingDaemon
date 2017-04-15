import json
import urllib
import datetime
import threading

REPORT_HTTPS = False
REPORT_DOMAIN = "whiteovaltechnologies.com"
REPORT_ENDPOINT = "iParkMobi-Demo-01/updateStatus.php"
REPORT_PARAM_NAME = "status"

def send_report(CCId, SensorID, OccState):
    parameterString = json.dumps({
        "ccid": CCId,
        "ts": int((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds()),
        "d": [{ "sid": SensorID, "eid": 0, "occ": OccState }]
        })
    print parameterString
    queryString = urllib.urlencode({REPORT_PARAM_NAME: parameterString})
    if REPORT_HTTPS:
        urlString = "https://"
    else:
        urlString = "http://"
    urlString += REPORT_DOMAIN+"/"+REPORT_ENDPOINT+"?"+queryString
    reader = urllib.urlopen(urlString)
    responseString = reader.read()
    print responseString
    if responseString == "\nSuccess!":
	return True
    else:
        return False

def threaded_send_report(CCId, SensorID, OccState):
    thread = threading.Thread(target=send_report, args = (CCId, SensorID, OccState))
    thread.daemon = True
    thread.start()

