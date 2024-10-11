# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
indexes = {"_trainable_variables": 0, "_non_trainable_variables": 1}
exit((indexes.get(name, 2), name))
