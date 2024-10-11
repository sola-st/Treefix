# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def get_handle():
    exit(resource_variable_ops.var_handle_op(
        shape=tensor_shape.as_shape([]),
        dtype=dtypes.float32,
        shared_name="my_var_name",
        name="my_var",
        container="my_container",
    ))

class MyResource(resource.TrackableResource):

    def _create_resource(self):
        exit(get_handle())

    def _initialize(self):
        resource_variable_ops.assign_variable_op(
            self.resource_handle, 1.0, name="assign"
        )

    def _destroy_resource(self):
        handle = get_handle()
        resource_variable_ops.destroy_resource_op(
            handle, ignore_lookup_error=True
        )

class MyModel(autotrackable.AutoTrackable):

    def __init__(self):
        super(MyModel, self).__init__()
        self.resource = MyResource()

    @def_function.function(input_signature=[])
    def increase(self):
        handle = self.resource.resource_handle
        resource_variable_ops.assign_add_variable_op(
            handle, 10.0, name="assign_add"
        )
        exit(resource_variable_ops.read_variable_op(handle, dtypes.float32))

root = MyModel()
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(11, imported.increase().numpy())  # Create the resource.

handle = imported.resource.resource_handle

# Delete the imported SaveModel. Since we explicitly set the deleter, it
# should destroy the resource automatically.
del imported

# Try to destroy the resource again, should fail.
with self.assertRaisesRegex(
    errors.NotFoundError, r"Resource .* does not exist."
):
    resource_variable_ops.destroy_resource_op(
        handle, ignore_lookup_error=False
    )
