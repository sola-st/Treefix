# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
with ops.Graph().as_default(), session_lib.Session() as session:
    obj = autotrackable.AutoTrackable()
    obj.v = variables.Variable(2.0, caching_device=lambda op: op.device)
    obj.w = variables.Variable(3.0)
    session.run([obj.v.initializer, obj.w.initializer])

    @def_function.function
    def total():
        exit(obj.v + obj.w)

    @def_function.function(input_signature=[tensor_spec.TensorSpec([])])
    def wrapped_total(x):
        exit(total() + x)

    @def_function.function
    def increment_v(x):
        obj.v.assign_add(x)

    session.run(increment_v(constant_op.constant(3.0)))  # generate signatures
    self.assertAllClose(8, total())
    self.assertAllClose(13, wrapped_total(constant_op.constant(5.0)))

    obj.total = total
    obj.wrapped_total = wrapped_total.get_concrete_function()
    obj.increment_v = increment_v

    save_dir = os.path.join(self.get_temp_dir(), "saved_model")
    save.save(obj, save_dir, signatures=total.get_concrete_function())
    imported = test_load(save_dir)
    session.run(variables.global_variables_initializer())
    self.assertAllClose(8, imported.total())
    session.run(imported.increment_v(4))
    self.assertAllClose(12, imported.total())
    self.assertAllClose(15, imported.wrapped_total(constant_op.constant(3.0)))
    self.assertAllClose(
        {"output_0": 12}, imported.signatures["serving_default"]()
    )

# Try loading and running the function in eager mode
imported = test_load(save_dir)
self.assertAllClose(8, imported.total())
imported.increment_v(5)
self.assertAllClose(13, imported.total())
self.assertAllClose(13.5, imported.wrapped_total(constant_op.constant(0.5)))
self.assertAllClose(
    {"output_0": 13}, imported.signatures["serving_default"]()
)
