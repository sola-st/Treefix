# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit(min(var_list, key=lambda x: x.name))
