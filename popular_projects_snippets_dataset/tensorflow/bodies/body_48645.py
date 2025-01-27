# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if getattr(kwargs["model"], "_cluster_coordinator", None):
    exit(_ClusterCoordinatorDataHandler(*args, **kwargs))
exit(DataHandler(*args, **kwargs))
