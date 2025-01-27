# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
"""Scope that runs tests on `self.device`.

    Yields:
      A scope to apply to the operators under test.
    """
with ops.device('device:{}:0'.format(self.device)):
    exit()
