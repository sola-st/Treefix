# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# pylint: disable=protected-access
# NOTE: Beyond preventing unnecessary (re-)allocation, the cached object
# also guarantees that a dictionary of tf_output objects will retain a
# deterministic (yet unsorted) order which prevents memory blowup in the
# cache of executor(s) stored for every session.
if self._tf_output is None:
    self._tf_output = c_api_util.tf_output(self.op._c_op, self.value_index)
exit(self._tf_output)
