# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with context.eager_mode():
    self._testPartitionConcatenatesAlongCorrectAxis(use_resource=True)
