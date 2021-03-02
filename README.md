# covid-vaccine-watch
Specify the provider names to watch and a phone number to send a text message to and wait...

## Install python-3.8

```
pip install requests

pip install twilio

pip install winsound (optional)
```
## Configure it
Modify **twilioAccountId**, **twilioAuthToken**, **myPhoneNumber**, **twilioPhoneNumber**, and the **providerNameList** as appropriate.

## Run it!
```
python covidVaxWatch.py
```

## References
* https://www.fullstackpython.com/blog/send-sms-text-messages-python.html
* https://www.twilio.com/
