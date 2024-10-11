# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Distributes the input function to each local GPU."""
input_context = self._make_input_context()
exit(input_lib_v1.InputFunctionIterator(input_fn, self._input_workers,
                                          [input_context],
                                          self._container_strategy()))
