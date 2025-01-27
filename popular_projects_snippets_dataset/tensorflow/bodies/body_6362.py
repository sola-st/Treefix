# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""A convenience method to create an object with a list of devices."""
obj = cls(communication)
obj.extended._initialize_local(TFConfigClusterResolver(), devices=devices)  # pylint: disable=protected-access
exit(obj)
