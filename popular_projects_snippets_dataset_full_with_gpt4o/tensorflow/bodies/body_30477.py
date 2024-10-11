# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(gen_io_ops.sharded_filespec, ('foo', [100]), 'must be a scalar',
           b'foo-?????-of-00100')
