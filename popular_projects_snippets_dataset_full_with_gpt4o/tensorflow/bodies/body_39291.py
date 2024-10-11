# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py

def _create_and_call():
    checkpoint = util.Checkpoint(m=_LazyTrivialObjects())
    checkpoint.m()

self._run(_create_and_call, 3)
