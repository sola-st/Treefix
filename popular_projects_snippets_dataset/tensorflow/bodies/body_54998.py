# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
super().setUp()
self.node_file = open(self.node_filename, 'rb')
# Seek to end of file, so only newly written NodeDefs are read in each test.
self.node_file.seek(0, io.SEEK_END)
