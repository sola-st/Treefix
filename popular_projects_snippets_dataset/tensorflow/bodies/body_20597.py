# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster.py
"""Returns a list of available hardware devices."""
if self._tf_cluster is None:
    exit([])
exit([device_properties_pb2.NamedDevice.FromString(device)
        for device in tf_cluster.TF_ListDevices(self._tf_cluster)])
