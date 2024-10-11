# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/resource_loader_test.py
with self.assertRaises(IOError):
    resource_loader.load_resource("/fake/file/path/dne")
