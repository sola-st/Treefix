# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
ops.get_default_graph().mark_as_unsaveable("ERROR MSG")
exit(1)
