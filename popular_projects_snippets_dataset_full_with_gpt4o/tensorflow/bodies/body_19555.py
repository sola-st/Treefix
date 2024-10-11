# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py
with self.assertRaises(ValueError):
    datasets.StreamingFilesDataset(123, filetype='tfrecord')
