# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
self._benchmarkGather('nontrivial_gather', axis, [9, 1, 0, 2] * 4,
                      use_xla_jit)
