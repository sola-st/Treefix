# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
self._train_fn_internal(iterator, iterator2)
while self.do_infinite_step:
    self._train_fn_internal(iterator, iterator2)
self.iterations.assign_add(1)
