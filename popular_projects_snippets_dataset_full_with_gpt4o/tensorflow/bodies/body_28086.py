# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py

def write_string_to_file(value, filename):
    with open(filename, "w") as f:
        f.write(value)

filenames = [
    os.path.join(self.get_temp_dir(), "file_%d.txt" % i) for i in range(5)
]
for filename in filenames:
    write_string_to_file(filename, filename)

dataset = (
    dataset_ops.Dataset.from_tensor_slices(filenames).map(
        io_ops.read_file, num_parallel_calls=2).prefetch(2).ignore_errors())
get_next = self.getNext(dataset)

# All of the files are present.
for filename in filenames:
    self.assertEqual(compat.as_bytes(filename), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

# Delete one of the files.
os.remove(filenames[0])

# Attempting to read filenames[0] will fail, but ignore_errors()
# will catch the error.
get_next = self.getNext(dataset)
for filename in filenames[1:]:
    self.assertEqual(compat.as_bytes(filename), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
