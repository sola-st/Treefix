# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
# Test that error is thrown when num fields doesn't match columns
column_names = ["col%d" % i for i in range(5)]
inputs = [[",".join(x for x in column_names), "0,1,2,3,4", "5,6,7,8,9"], [
    ",".join(x for x in column_names), "10,11,12,13,14", "15,16,17,18,19"
]]
filenames = self._setup_files(inputs)
with self.assertRaises(ValueError):
    self._make_csv_dataset(
        filenames,
        column_names=column_names + ["extra_name"],
        column_defaults=None,
        batch_size=2,
        num_epochs=10)
