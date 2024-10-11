# Extracted from https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror
import certifi
import ssl
import urllib
context = ssl.create_default_context(cafile=certifi.where())
result = urllib.request.urlopen('https://www.example.com', context=context)

import os
import certifi
import urllib
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
os.environ["SSL_CERT_FILE"] = certifi.where()
result = urllib.request.urlopen('https://www.example.com')


import certifi
import ssl
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
result = urllib.request.urlopen('https://www.example.com')

sudo update-ca-certificates --fresh
export SSL_CERT_DIR=/etc/ssl/certs

cd "/Applications/$(python3 --version | awk '{print $2}'| awk  -F. '{print "Python " $1"."$2}')"
sudo "./Install Certificates.command"

