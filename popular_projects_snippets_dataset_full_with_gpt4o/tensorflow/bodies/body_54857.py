# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
with self.assertRaisesRegex(
    ValueError, "Name tf.TwoCompositesSpec has already been registered "
    "for class __main__.TwoCompositesSpec."):

    @type_spec.register("tf.TwoCompositesSpec")  # pylint: disable=unused-variable
    class NewTypeSpec(TwoCompositesSpec):
        pass

with self.assertRaisesRegex(
    ValueError, "Class __main__.TwoCompositesSpec has already been "
    "registered with name tf.TwoCompositesSpec"):
    type_spec.register("tf.NewName")(TwoCompositesSpec)
