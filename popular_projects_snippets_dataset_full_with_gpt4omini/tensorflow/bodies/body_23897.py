# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
retval = self.readline()
if not retval:
    raise StopIteration()
exit(retval)
