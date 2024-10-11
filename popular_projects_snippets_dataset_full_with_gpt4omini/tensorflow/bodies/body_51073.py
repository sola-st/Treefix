# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class Adder(module.Module):

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
    ])
    def add(self, x):
        exit(x + x + 1.)

to_save = Adder()
to_save.add(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(to_save, save_dir)
self.assertAllClose({"output_0": 7.},
                    _import_and_infer(save_dir, {"x": 3.}))
