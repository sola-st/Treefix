# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()

# Usage pattern:
# * Nodes a_i are constants defined at the outermost scope, and are used
#   as control inputs for the ith nested scope.
# * Nodes b_i are defined as Mul(a_3, a_4) at each scope.
# * Nodes c_i are defined as Mul(a_1, b_1) at each scope.
# * Nodes d_i are defined as Mul(b_i, c_i) at each scope.
# * Nodes e_i are defined as Mul(e_i-1, e_i-1) at each scope i > 1.

a_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
a_2 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
a_3 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
a_4 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

with g.control_dependencies([a_1]):
    b_1 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_3, a_4],
                    [dtypes.float32])
    c_1 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_1, b_1],
                    [dtypes.float32])
    d_1 = _apply_op(g, "TwoFloatInputsFloatOutput", [b_1, c_1],
                    [dtypes.float32])
    e_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])
    with g.control_dependencies([a_2]):
        b_2 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_3, a_4],
                        [dtypes.float32])
        c_2 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_1, b_1],
                        [dtypes.float32])
        d_2 = _apply_op(g, "TwoFloatInputsFloatOutput", [b_2, c_2],
                        [dtypes.float32])
        e_2 = _apply_op(g, "TwoFloatInputsFloatOutput", [e_1, e_1],
                        [dtypes.float32])
        with g.control_dependencies([a_3]):
            b_3 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_3, a_4],
                            [dtypes.float32])
            c_3 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_1, b_1],
                            [dtypes.float32])
            d_3 = _apply_op(g, "TwoFloatInputsFloatOutput", [b_3, c_3],
                            [dtypes.float32])
            e_3 = _apply_op(g, "TwoFloatInputsFloatOutput", [e_2, e_2],
                            [dtypes.float32])
            with g.control_dependencies([a_4]):
                b_4 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_3, a_4],
                                [dtypes.float32])
                c_4 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_1, b_1],
                                [dtypes.float32])
                d_4 = _apply_op(g, "TwoFloatInputsFloatOutput", [b_4, c_4],
                                [dtypes.float32])
                e_4 = _apply_op(g, "TwoFloatInputsFloatOutput", [e_3, e_3],
                                [dtypes.float32])

self.assertItemsEqual([a_1.op], b_1.op.control_inputs)
self.assertItemsEqual([a_1.op, a_2.op], b_2.op.control_inputs)
self.assertItemsEqual([a_1.op, a_2.op], b_3.op.control_inputs)
self.assertItemsEqual([a_1.op, a_2.op], b_4.op.control_inputs)

self.assertItemsEqual([], c_1.op.control_inputs)
self.assertItemsEqual([a_2.op], c_2.op.control_inputs)
self.assertItemsEqual([a_2.op, a_3.op], c_3.op.control_inputs)
self.assertItemsEqual([a_2.op, a_3.op, a_4.op], c_4.op.control_inputs)

self.assertItemsEqual([], d_1.op.control_inputs)
self.assertItemsEqual([], d_2.op.control_inputs)
self.assertItemsEqual([], d_3.op.control_inputs)
self.assertItemsEqual([], d_4.op.control_inputs)

self.assertItemsEqual([a_1.op], e_1.op.control_inputs)
self.assertItemsEqual([a_2.op], e_2.op.control_inputs)
self.assertItemsEqual([a_3.op], e_3.op.control_inputs)
self.assertItemsEqual([a_4.op], e_4.op.control_inputs)
