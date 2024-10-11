# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    x = constant_op.constant(2.0, shape=[6], name="input")
    id_op = array_ops.identity(x, name="id")
self.assertTrue(isinstance(id_op.op.inputs[0], ops.Tensor))
self.assertProtoEquals("name: 'id' op: 'Identity' input: 'input' "
                       "attr { key: 'T' value { type: DT_FLOAT } }",
                       id_op.op.node_def)
