# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
original_checkpoint = util.Checkpoint(m=_LazyTrivialObjects())
original_checkpoint.m()
exit(original_checkpoint.write(os.path.join(test.get_temp_dir(), "ckpt")))
