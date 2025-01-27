# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    in_eager_mode = context.executing_eagerly()
    ta = _make_ta(3, "foo")
    with self.assertRaisesOpError(
        r"Expected lengths to be a vector, received shape: \[\]"):
        if in_eager_mode:
            self.evaluate(ta.split([1.0, 2.0, 3.0], 1))
        else:
            lengths = array_ops.placeholder(dtypes.int64)
            ta.split([1.0, 2.0, 3.0], lengths).flow.eval(feed_dict={lengths: 1})

    error_msg = ("Unused values in tensor. Length of tensor: 3 Values used: 1"
                 if control_flow_util.ENABLE_CONTROL_FLOW_V2 and
                 not in_eager_mode else
                 r"Expected sum of lengths to be equal to values.shape\[0\], "
                 r"but sum of lengths is 1 and value's shape is: \[3\]")
    with self.assertRaisesOpError(error_msg):
        self.evaluate(ta.split([1.0, 2.0, 3.0], [1]).flow)

    ta = _make_ta(1, "baz")
    if control_flow_util.ENABLE_CONTROL_FLOW_V2 and not in_eager_mode:
        with self.assertRaisesRegex(
            ValueError, "Shape must be at least rank 1 but is rank 0"):
            self.evaluate(ta.split(1.0, [1]).flow)
    else:
        with self.assertRaisesOpError(
            r"Expected value to be at least a vector, but received shape: \[\]"
        ):
            self.evaluate(ta.split(1.0, [1]).flow)

    if not control_flow_util.ENABLE_CONTROL_FLOW_V2 or in_eager_mode:
        ta = _make_ta(2, "buz")
        with self.assertRaisesOpError(
            r"TensorArray's size is not equal to the size of lengths "
            r"\(2 vs. 1\), and the TensorArray is not marked as "
            r"dynamically resizeable"):
            self.evaluate(ta.split([1.0], [1]).flow)
