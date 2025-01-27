# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class HasDataset(module.Module):

    def __init__(self, temp_dir, file_name):
        super(HasDataset, self).__init__()
        file = os.path.join(temp_dir, file_name)
        with tf_record.TFRecordWriter(file, "GZIP") as f:
            for v in ["a", "aa", "aaa"]:
                f.write(str(v))
        self.dataset = readers.TFRecordDataset([file], compression_type="GZIP")

    @def_function.function
    def __call__(self, x):
        current_sum = array_ops.zeros([], dtype=dtypes.int32)
        for element in self.dataset:
            current_sum += x * string_ops.string_length(element)
        exit(current_sum)

temp_dir = self.get_temp_dir()
file_name = "tf_record_asset.tfrecord.gz"
root = HasDataset(temp_dir, file_name)
self.assertEqual(
    18,  # 3 * (1 + 2 + 3)
    root(constant_op.constant(3, dtype=dtypes.int32)).numpy(),
)

save_dir = os.path.join(self.get_temp_dir(), "save_dir")
save.save(root, save_dir)

file_io.delete_file(os.path.join(temp_dir, file_name))
asset_path = os.path.join(save_dir, "assets/{}".format(file_name))
self.assertTrue(file_io.file_exists(asset_path))
load_dir = os.path.join(self.get_temp_dir(), "load_dir")
file_io.rename(save_dir, load_dir)

loaded = test_load(load_dir, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(
    18,  # 3 * (1 + 2 + 3)
    loaded(constant_op.constant(3, dtype=dtypes.int32)).numpy(),
)
