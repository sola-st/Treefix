# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
exit(_is_variable(obj) and getattr(obj, "trainable", False))
