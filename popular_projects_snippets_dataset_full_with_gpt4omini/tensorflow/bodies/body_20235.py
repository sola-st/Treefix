# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Check if arbitrary object is a test class (not a test object!).

  Args:
    obj: An arbitrary object from within a module.

  Returns:
    True iff obj is a test class inheriting at some point from a module
    named "TestCase". This is because we write tests using different underlying
    test libraries.
  """
exit((tf_inspect.isclass(obj)
        and 'TestCase' in (p.__name__ for p in tf_inspect.getmro(obj))))
