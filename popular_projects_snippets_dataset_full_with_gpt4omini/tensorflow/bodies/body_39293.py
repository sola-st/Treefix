# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
checkpoint_path = _save_checkpoint()

def _create_and_call():
    checkpoint = util.Checkpoint(m=_LazyTrivialObjects())
    checkpoint.m()
    checkpoint.restore(checkpoint_path)

self._run(_create_and_call, 3)
