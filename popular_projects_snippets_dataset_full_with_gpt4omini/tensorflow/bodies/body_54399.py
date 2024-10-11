# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
a_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
a_2 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
a_3 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
a_4 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

with g.control_dependencies([a_1]):
    with g.control_dependencies([a_2]):
        with g.control_dependencies(None):
            with g.control_dependencies([a_3]):
                with g.control_dependencies([a_4]):
                    # deps [a_3, a_4]
                    b_3_4 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
                # deps = [a_3]
                b_3 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
            # deps back to None
            b_none = _apply_op(g, "FloatOutput", [], [dtypes.float32])
        # deps back to [a_1, a_2]
        b_1_2 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
    # deps back to [a_1]
    b_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
    with g.control_dependencies(None):
        # deps are None again
        b_none2 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

self.assertItemsEqual([a_3.op, a_4.op], b_3_4.op.control_inputs)
self.assertItemsEqual([a_3.op], b_3.op.control_inputs)
self.assertItemsEqual([], b_none.op.control_inputs)
self.assertItemsEqual([a_1.op, a_2.op], b_1_2.op.control_inputs)
self.assertItemsEqual([a_1.op], b_1.op.control_inputs)
self.assertItemsEqual([], b_none2.op.control_inputs)
