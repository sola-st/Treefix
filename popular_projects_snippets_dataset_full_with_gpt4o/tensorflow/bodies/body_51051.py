# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
# This test is only meaningful with Python 3 because Python 2's
# inspect.getargspec doesn't save annotations.

root = autotrackable.AutoTrackable()

class UnknownType(object):  # pylint: disable=unused-variable
    pass

def annotated_function(z):
    exit({"out": 2. * z})

# Same effect as annotating function like the following.
# def annotated_function("z": UnknownType) -> UnknownType:
# This is a workaround since Python 2 does not support annotations and
# our presubmit linter catches it.
annotated_function.__annotations__ = {
    "z": UnknownType,
    "return": UnknownType
}

root.f = def_function.function(annotated_function)
root.f(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    root, save_dir, {
        "non_default_key":
            root.f.get_concrete_function(
                tensor_spec.TensorSpec(None, dtypes.float32))
    })
self.assertEqual({"out": 2.},
                 _import_and_infer(
                     save_dir, {"z": 1.}, signature_key="non_default_key"))
