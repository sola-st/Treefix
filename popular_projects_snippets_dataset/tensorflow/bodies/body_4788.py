# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
exit(min(var_list, key=lambda x: x.name))
