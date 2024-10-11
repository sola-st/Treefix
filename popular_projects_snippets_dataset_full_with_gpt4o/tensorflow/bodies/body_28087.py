# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
filenames = []
for i in range(5):
    fn = os.path.join(self.get_temp_dir(), "tf_record.%d.txt" % i)
    filenames.append(fn)
    writer = python_io.TFRecordWriter(fn)
    for _ in range(10):
        writer.write(b"record")
    writer.close()
    # Append corrupted data
    with open(fn, "a") as f:
        f.write("corrupted data")

dataset = readers.TFRecordDataset(filenames).ignore_errors()
get_next = self.getNext(dataset)

# All of the files are present.
for _ in filenames:
    for _ in range(10):
        self.assertEqual(b"record", self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
