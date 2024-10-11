# Extracted from ./data/repos/pandas/pandas/io/common.py
self.buffer = buffer
self.encoding = encoding
# Because a character can be represented by more than 1 byte,
# it is possible that reading will produce more bytes than n
# We store the extra bytes in this overflow variable, and append the
# overflow to the front of the bytestring the next time reading is performed
self.overflow = b""
