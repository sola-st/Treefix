# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
if self._shared_input_branch_func():
    self._shared_input_branch = self._shared_input_branch_func()
self._branch_a = self._branch_a_func()
self._branch_b = self._branch_b_func()

if self._shared_output_branch_func():
    self._shared_output_branch = self._shared_output_branch_func()
