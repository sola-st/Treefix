# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
self.skipTest("b/216201668: revisit parallel device and saved model")

different_values = self.device.pack(
    [constant_op.constant(-1.),
     constant_op.constant(3.)])
with self.device:
    m = module.Module()
    m.v = variables.Variable(different_values)
    m.f = def_function.function(lambda: m.v * 2.)
    self.assertAllClose([-2., 6.], self.device.unpack(m.f()))
saved_model_path = os.path.join(self.get_temp_dir(), "saved_model")
save.save(m, saved_model_path)

context._reset_context()
self.setUp()

single_device_loaded = load.load(saved_model_path)
self.assertAllClose(-2., single_device_loaded.f())
assign_value = self.device.pack(
    [constant_op.constant(.1), constant_op.constant(.2)])
with self.device:
    parallel_loaded = load.load(saved_model_path)
    self.assertAllClose([-2., 6.], self.device.unpack(parallel_loaded.f()))
    self.assertAllClose([-1., 3.], self.device.unpack(parallel_loaded.v))
    parallel_loaded.v.assign(assign_value)
    self.assertAllClose([.2, .4], self.device.unpack(parallel_loaded.f()))
