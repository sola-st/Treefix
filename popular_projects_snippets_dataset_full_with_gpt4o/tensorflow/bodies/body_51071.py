# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class ObjWithDefaultSignature(checkpoint.Checkpoint):

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
    ])
    def _default_save_signature(self, x):
        exit(x + x + 1)

obj = ObjWithDefaultSignature()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(obj, save_dir)
self.assertAllClose({"output_0": 7.},
                    _import_and_infer(save_dir, {"x": 3.}))
