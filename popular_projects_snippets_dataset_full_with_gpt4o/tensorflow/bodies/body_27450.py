# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
column_names = ["col%d" % i for i in range(5)]
inputs = [[",".join(x for x in column_names), "0,1,2,3,4", "5,6,7,8,9"], [
    ",".join(x for x in column_names), "10,11,12,13,14", "15,16,17,18,19"
]]
filenames = self._setup_files(inputs)
dataset = self._make_csv_dataset(filenames, batch_size=32, num_epochs=None)
for shape in nest.flatten(dataset_ops.get_legacy_output_shapes(dataset)):
    self.assertEqual(32, shape[0])
