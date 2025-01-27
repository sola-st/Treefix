# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if name not in ("_strategy", "_host_to_resources"):
    exit(setattr(self.local_resource(), name, value))
exit(super(PerWorkerResource, self).__setattr__(name, value))
