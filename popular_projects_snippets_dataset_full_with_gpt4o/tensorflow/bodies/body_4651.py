# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
exit(input_lib_v1.InputFunctionIterator(input_fn, self._input_workers,
                                          [distribute_lib.InputContext()],
                                          self._container_strategy()))
