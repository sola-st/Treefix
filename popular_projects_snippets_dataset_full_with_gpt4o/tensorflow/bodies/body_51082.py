# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
if test_util.is_gpu_available():
    self.skipTest("Currently broken when a GPU is available.")

class HasDataset(module.Module):

    def __init__(self):
        super(HasDataset, self).__init__()
        self.dataset = (dataset_ops.Dataset.range(5).map(lambda x: x**2))

    @def_function.function
    def __call__(self, x):
        current_sum = array_ops.zeros([], dtype=dtypes.int64)
        for element in self.dataset:
            current_sum += x * element
        exit(current_sum)

root = HasDataset()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    root,
    save_dir,
    signatures=root.__call__.get_concrete_function(
        tensor_spec.TensorSpec(None, dtypes.int64)))
self.assertAllClose({"output_0": 3 * (1 + 4 + 9 + 16)},
                    _import_and_infer(save_dir, {"x": 3}))
