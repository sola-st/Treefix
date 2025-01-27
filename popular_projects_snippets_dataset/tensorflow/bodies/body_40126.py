# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
c = constant_op.constant(1.)
with forwardprop.ForwardAccumulator(c, 10.) as acc:
    packed_input_tangents = forwardprop_util.pack_tangents([c]).tangents
    self.assertAllClose([10.], packed_input_tangents)
    d = constant_op.constant(2.)
    d_tangent = constant_op.constant(3.)
    tape_lib.record_operation_forwardprop_only("FunctionWithInlineJVPs",
                                               [d] + [d_tangent],
                                               [c] + packed_input_tangents,
                                               None, (((0, 1),),))
    self.assertAllClose(3., acc.jvp(d))
