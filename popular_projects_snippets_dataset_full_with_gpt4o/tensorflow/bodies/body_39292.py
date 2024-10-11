# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
checkpoint = util.Checkpoint(m=_LazyTrivialObjects())
checkpoint.m()
checkpoint.restore(checkpoint_path)
