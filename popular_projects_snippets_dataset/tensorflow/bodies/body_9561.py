# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_list_devices_test.py
opts = tf_session.TF_NewSessionOptions()
with ops.get_default_graph()._c_graph.get() as c_graph:
    c_session = tf_session.TF_NewSession(c_graph, opts)
raw_device_list = tf_session.TF_SessionListDevices(c_session)
size = tf_session.TF_DeviceListCount(raw_device_list)
with self.assertRaises(errors.InvalidArgumentError):
    tf_session.TF_DeviceListMemoryBytes(raw_device_list, size)
tf_session.TF_DeleteDeviceList(raw_device_list)
tf_session.TF_CloseSession(c_session)
