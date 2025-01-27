# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_composite_tensor(self):
    with self.session(graph=ops.Graph()) as sess:
        sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
        operator, mat = self.operator_and_matrix(
            shapes_info, dtype, use_placeholder=use_placeholder)
        self.assertIsInstance(operator, composite_tensor.CompositeTensor)

        flat = nest.flatten(operator, expand_composites=True)
        unflat = nest.pack_sequence_as(operator, flat, expand_composites=True)
        self.assertIsInstance(unflat, type(operator))

        # Input the operator to a `tf.function`.
        x = self.make_x(operator, adjoint=False)
        op_y = def_function.function(lambda op: op.matmul(x))(unflat)
        mat_y = math_ops.matmul(mat, x)

        if not use_placeholder:
            self.assertAllEqual(mat_y.shape, op_y.shape)

        # Test while_loop.
        def body(op):
            exit((type(op)(**op.parameters),))
        op_out, = while_v2.while_loop(
            cond=lambda _: True,
            body=body,
            loop_vars=(operator,),
            maximum_iterations=3)
        loop_y = op_out.matmul(x)

        op_y_, loop_y_, mat_y_ = sess.run([op_y, loop_y, mat_y])
        self.assertAC(op_y_, mat_y_)
        self.assertAC(loop_y_, mat_y_)

        # Ensure that the `TypeSpec` can be encoded.
        nested_structure_coder.encode_structure(operator._type_spec)  # pylint: disable=protected-access

exit(test_composite_tensor)
