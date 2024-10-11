# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
copied_variables = copy.deepcopy(self._variables, memo)
exit(DistributedVariable(
    copied_variables, enable_packed_handle=self._packed_handle is not None))
