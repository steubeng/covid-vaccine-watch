import requests 
from twilio.rest import Client
import time
import datetime
# import winsound

# https://www.fullstackpython.com/blog/send-sms-text-messages-python.html
twilioAccountId = ""
twilioAuthToken = ""
twilioClient = Client(twilioAccountId, twilioAuthToken)
backendApiCall = "https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers"
myPhoneNumber = ""
twilioPhoneNumber = ""
providerNameList = [
    "SUNY Albany ",
    "SUNY Albany"
]
delay = 120
PROVIDER_LIST = "providerList"
PROVIDER_NAME = "providerName"
AVAILABLE_APPOINTMENTS = "availableAppointments"
APPOINTMENTS_AVAILABLE_CODE = "Y"
NO_APPOINTMENTS_CURRENTLY_CODE = "N"

while (True):
    response = requests.get(backendApiCall) 
    providerList = response.json()[PROVIDER_LIST]
    for i in range(len(providerList)):
        providerName = providerList[i][PROVIDER_NAME]
        if (providerName in providerNameList):
            availableAppointments = providerList[i][AVAILABLE_APPOINTMENTS]            
            if (availableAppointments == APPOINTMENTS_AVAILABLE_CODE):
                print("Appointments Available at '" + providerName + "'!")
                twilioClient.messages.create(
                    to=myPhoneNumber,
                    from_=twilioPhoneNumber,
                    body="Appointments Available at '" + providerName + "'!  Go to https://am-i-eligible.covid19vaccine.health.ny.gov/ to reserve a spot now!")
                # while(True):
                #     winsound.PlaySound('ding.wav', winsound.SND_FILENAME)
                exit()
            if (availableAppointments == NO_APPOINTMENTS_CURRENTLY_CODE):
                datetime_object = datetime.datetime.now()
                print("None Available Currently for '" + providerName + "' as of", datetime_object)
    time.sleep(delay)
