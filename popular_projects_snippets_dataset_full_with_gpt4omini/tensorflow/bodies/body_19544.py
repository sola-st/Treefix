# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py
all_contents = []
for i in range(_NUM_FILES):
    filename = os.path.join(self.get_temp_dir(), 'text_line.%d.txt' % i)
    contents = []
    for j in range(_NUM_ENTRIES):
        contents.append(compat.as_bytes('%d: %d' % (i, j)))
    with open(filename, 'wb') as f:
        f.write(b'\n'.join(contents))
    all_contents.extend(contents)

dataset = datasets.StreamingFilesDataset(
    os.path.join(self.get_temp_dir(), 'text_line.*.txt'), filetype='text')

with ops.device(self._worker_device):
    iterator = dataset_ops.make_initializable_iterator(dataset)
self._sess.run(iterator.initializer)
get_next = iterator.get_next()

retrieved_values = []
for _ in range(4 * len(all_contents)):
    retrieved_values.append(compat.as_bytes(self._sess.run(get_next)))

self.assertEqual(set(all_contents), set(retrieved_values))
