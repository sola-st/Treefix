# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
"""Benchmarks a gather op that's really a dynamic slice."""
self._benchmarkGather('slice_gather', axis, [1], use_xla_jit)
