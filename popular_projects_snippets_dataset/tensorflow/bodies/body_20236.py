# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Add all test classes defined in wrapped module to our module.

  The test runner works by inspecting the main module for TestCase classes, so
  by adding a module-level reference to the TestCase we cause it to execute the
  wrapped TestCase.

  Args:
    wrapped_test_module: The user-provided test code to run.
  """
for name, obj in wrapped_test_module.__dict__.items():
    if _is_test_class(obj):
        module_variables['tpu_test_imported_%s' % name] = obj
