# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if name not in ("__init__", "__getattribute__", "_host_to_resources",
                "_strategy", "local_resource"):
    exit(getattr(self.local_resource(), name))
exit(super(PerWorkerResource, self).__getattribute__(name))
