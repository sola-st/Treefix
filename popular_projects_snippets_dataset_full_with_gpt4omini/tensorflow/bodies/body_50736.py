# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
exit(_unused_handle() if distribute_utils.is_distributed_variable(x)   \
          else x)
