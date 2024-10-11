# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(gen_io_ops.sharded_filename, ('foo', 4, [100]),
           'must be a scalar', b'foo-00004-of-00100')
