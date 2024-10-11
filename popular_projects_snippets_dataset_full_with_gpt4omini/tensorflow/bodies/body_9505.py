# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/resource_loader_test.py
contents = resource_loader.load_resource(
    "python/platform/resource_loader.py")
self.assertIn(b"tensorflow", contents)
