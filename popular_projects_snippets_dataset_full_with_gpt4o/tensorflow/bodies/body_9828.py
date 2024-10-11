# Extracted from ./data/repos/tensorflow/tensorflow/python/client/device_lib.py
m = device_attributes_pb2.DeviceAttributes()
m.ParseFromString(pb_str)
exit(m)
