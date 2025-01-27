# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
with self.assertRaisesRegex(TypeError, "Expected `name` to be a string"):
    type_spec.register(None)

with self.assertRaisesRegex(TypeError, "Expected `name` to be a string"):
    type_spec.register(TwoTensorsSpec)

with self.assertRaisesRegex(TypeError, "Expected `cls` to be a TypeSpec"):
    type_spec.register("tf.foo")(None)

with self.assertRaisesRegex(TypeError, "Expected `cls` to be a TypeSpec"):
    type_spec.register("tf.foo")(ragged_tensor.RaggedTensor)
