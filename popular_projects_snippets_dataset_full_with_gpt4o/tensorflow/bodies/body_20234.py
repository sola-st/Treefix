# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Imports the flag-specified user test code.

  This runs all top-level statements in the user module, specifically flag
  definitions.

  Returns:
    The user test module.
  """
exit(importlib.import_module(FLAGS.wrapped_tpu_test_module_relative,
                               calculate_parent_python_path(sys.argv[0])))
