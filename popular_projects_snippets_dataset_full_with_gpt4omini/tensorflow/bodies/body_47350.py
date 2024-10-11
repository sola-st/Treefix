# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
super(_MultiIOSubclassModelCustomBuild, self).__init__()
self._shared_input_branch_func = shared_input_branch_func
self._branch_a_func = branch_a_func
self._branch_b_func = branch_b_func
self._shared_output_branch_func = shared_output_branch_func

self._shared_input_branch = None
self._branch_a = None
self._branch_b = None
self._shared_output_branch = None
