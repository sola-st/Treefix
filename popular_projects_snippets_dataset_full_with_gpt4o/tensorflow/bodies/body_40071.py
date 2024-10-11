# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
sum_outputs = (constant_op.constant(6.),)

with self.assertRaisesRegex(ValueError, r".*was expected to be of shape*"):
    forwardprop._jvp_dispatch(
        op_name="Add",
        attr_tuple=(),
        inputs=(constant_op.constant(2.), constant_op.constant(4.)),
        outputs=sum_outputs,
        tangents=(constant_op.constant([1., 2.]),
                  constant_op.constant([[1.], [2.]])),
        use_batch=True)
