# Extracted from https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
byte_value = b"abcde"
print("Initial value = {}".format(byte_value))
print("Initial value type = {}".format(type(byte_value)))
string_value = byte_value.decode("utf-8")
# utf-8 is used here because it is a very common encoding, but you need to use the encoding your data is actually in.
print("------------")
print("Converted value = {}".format(string_value))
print("Converted value type = {}".format(type(string_value)))

Initial value = b'abcde'
Initial value type = <class 'bytes'>
------------
Converted value = abcde
Converted value type = <class 'str'>

