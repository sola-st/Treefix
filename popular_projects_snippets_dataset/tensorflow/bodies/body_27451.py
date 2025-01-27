# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
data = [[
    "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19",
    "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19"
]]
file_path = self._setup_files(data)

ds = readers.make_csv_dataset(
    file_path, batch_size=1, shuffle=False, num_epochs=1)
nxt = self.getNext(ds)

result = list(self.evaluate(nxt()).values())

self.assertEqual(result, sorted(result))
