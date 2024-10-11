# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
"""Prints dictionary with formatting (2 column table).

  Args:
    py_dict: Dictionary that is to be printed out in a table format.
  """
for gpu, cc in py_dict.items():
    print("{:<25}{:<25}".format(gpu, cc))
