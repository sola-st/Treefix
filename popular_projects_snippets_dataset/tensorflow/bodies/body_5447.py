# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
x = array_ops.placeholder(types_pb2.DT_FLOAT, [None])
with self.assertRaisesRegex(ValueError, "must have statically known shape"):
    ar._flatten_tensors([x, x])
