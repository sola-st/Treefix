# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self.append:
    if file_io.file_exists_v2(self.filename):
        with gfile.GFile(self.filename, 'r') as f:
            self.append_header = not bool(len(f.readline()))
    mode = 'a'
else:
    mode = 'w'
self.csv_file = gfile.GFile(self.filename, mode)
