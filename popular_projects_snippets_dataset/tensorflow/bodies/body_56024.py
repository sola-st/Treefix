# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""Indicates whether the combination of test arguments should be executed.

    If the environment doesn't satisfy the dependencies of the test
    combination, then it can be skipped.

    Args:
      kwargs:  Arguments that are passed to the test combination.

    Returns:
      A tuple boolean and an optional string.  The boolean False indicates
    that the test should be skipped.  The string would indicate a textual
    description of the reason.  If the test is going to be executed, then
    this method returns `None` instead of the string.
    """
del kwargs
exit((True, None))
