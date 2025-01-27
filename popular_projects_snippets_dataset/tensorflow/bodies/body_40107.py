# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
two = constant_op.constant(2.)
primal_in = constant_op.constant(1.)
inner_jvp = constant_op.constant(3.)
with forwardprop.ForwardAccumulator(
    [primal_in, inner_jvp],
    [constant_op.constant(2.),
     constant_op.constant(4.)]) as outer_acc:
    with forwardprop.ForwardAccumulator(primal_in, inner_jvp) as inner_acc:
        packed_input_indices, packed_input_tangents = (
            forwardprop_util.pack_tangents([primal_in]))
        self.assertAllClose([3., 2., 4.], packed_input_tangents)
        expected_indices = (
            # inner_acc watches primal_in
            (
                (0, 1),),
            # outer_acc watches primal_in and inner_jvp
            ((0, 2), (1, 3)))
        self.assertAllEqual(expected_indices, packed_input_indices)
        primal_out = primal_in * two
        self.assertAllClose(6., inner_acc.jvp(primal_out))
        self.assertAllClose(4., outer_acc.jvp(primal_out))
        self.assertAllClose(8., outer_acc.jvp(inner_acc.jvp(primal_out)))
        packed_output_indices, packed_output_tangents = (
            forwardprop_util.pack_tangents([primal_out]))
        self.assertAllClose([6., 4., 8.], packed_output_tangents)
        self.assertAllEqual(expected_indices, packed_output_indices)
