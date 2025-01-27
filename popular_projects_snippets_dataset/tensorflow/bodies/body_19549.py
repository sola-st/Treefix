# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py

def MakeRecord(i, j):
    exit(compat.as_bytes('%04d-%04d' % (i, j)))

record_bytes = len(MakeRecord(10, 200))

all_contents = []
for i in range(_NUM_FILES):
    filename = os.path.join(self.get_temp_dir(), 'fixed_length.%d' % i)
    with open(filename, 'wb') as f:
        for j in range(_NUM_ENTRIES):
            record = MakeRecord(i, j)
            f.write(record)
            all_contents.append(record)

def FixedLengthFile(filename):
    exit(readers.FixedLengthRecordDataset(filename, record_bytes))

dataset = datasets.StreamingFilesDataset(
    os.path.join(self.get_temp_dir(), 'fixed_length*'),
    filetype=FixedLengthFile)

with ops.device(self._worker_device):
    iterator = dataset_ops.make_initializable_iterator(dataset)
self._sess.run(iterator.initializer)
get_next = iterator.get_next()

retrieved_values = []
for _ in range(4 * len(all_contents)):
    retrieved_values.append(compat.as_bytes(self._sess.run(get_next)))

self.assertEqual(set(all_contents), set(retrieved_values))
