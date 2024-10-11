# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class HasDatastructures(checkpoint.Checkpoint):

    def __init__(self):
        self.a = [1.]
        self.a.append(variables.Variable(2.))
        self.b = {"a": variables.Variable(3.)}

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
    ])
    def add(self, x):
        exit(x + math_ops.add_n(self.a) + self.b["a"])

to_save = HasDatastructures()
to_save.add(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(to_save, save_dir)
self.assertAllClose({"output_0": 10.},
                    _import_and_infer(save_dir, {"x": 4.}))
