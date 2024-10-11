# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self.sep = separator
self.filename = path_to_string(filename)
self.append = append
self.writer = None
self.keys = None
self.append_header = True
super(CSVLogger, self).__init__()
