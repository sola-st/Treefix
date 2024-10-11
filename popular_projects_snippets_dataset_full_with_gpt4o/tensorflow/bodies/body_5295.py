# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary._as_graph_element())  # pylint: disable=protected-access
if self._policy:
    exit(self._policy._as_graph_element(self))  # pylint: disable=protected-access

raise NotImplementedError(
    "DistributedVariable._as_graph_element requires a valid "
    "VariablePolicy. Please set the policy via the `var_policy` argument "
    "in the constructor, or override this method in sub-classes which "
    "support cross-replica accesses.")
