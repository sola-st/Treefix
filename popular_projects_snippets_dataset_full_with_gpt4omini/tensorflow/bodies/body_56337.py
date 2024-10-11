# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
# Note: "_" isn't a valid tensor name, but it is a valid python symbol
# name; and tf.function constructs TensorSpecs using function argument
# names.
for name in ["beep", "foo/bar:0", "a-b_c/d", "_"]:
    desc = tensor_spec.TensorSpec([1], dtypes.float32, name=name)
    self.assertEqual(desc.name, name)
