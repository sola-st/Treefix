# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
if isinstance(obj, metrics_mod.Metric):
    exit(obj.__class__.from_config(obj.get_config()))
exit(obj)  # Can be a function or `None`.
