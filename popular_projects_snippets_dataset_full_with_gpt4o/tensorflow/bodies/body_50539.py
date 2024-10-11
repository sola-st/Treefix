# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(RemoteMonitor, self).__init__()

self.root = root
self.path = path
self.field = field
self.headers = headers
self.send_as_json = send_as_json
