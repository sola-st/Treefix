# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
named_device = device_properties_pb2.NamedDevice()
named_device.name = '/GPU:0'
named_device.properties.type = 'GPU'
named_device.properties.num_cores = 24
named_device.properties.frequency = 1000
named_device.properties.environment['architecture'] = '4'
cluster = gcluster.Cluster(devices=[named_device])
exit(cluster)
