import kubernetes
from kubernetes import client, config
import urllib3
import sys
import json
import os

username = os.environ['SANT_01_SERVICE_HOST']

print(username)

