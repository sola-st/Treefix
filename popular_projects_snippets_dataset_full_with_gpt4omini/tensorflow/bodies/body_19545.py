# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py
all_contents = []
for i in range(_NUM_FILES):
    filename = os.path.join(self.get_temp_dir(), 'tf_record.%d' % i)
    writer = python_io.TFRecordWriter(filename)
    for j in range(_NUM_ENTRIES):
        record = compat.as_bytes('Record %d of file %d' % (j, i))
        writer.write(record)
        all_contents.append(record)
    writer.close()

dataset = datasets.StreamingFilesDataset(
    os.path.join(self.get_temp_dir(), 'tf_record*'), filetype='tfrecord')

with ops.device(self._worker_device):
    iterator = dataset_ops.make_initializable_iterator(dataset)
self._sess.run(iterator.initializer)
get_next = iterator.get_next()

retrieved_values = []
for _ in range(4 * len(all_contents)):
    retrieved_values.append(compat.as_bytes(self._sess.run(get_next)))

self.assertEqual(set(all_contents), set(retrieved_values))
