# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py
with self.assertRaises(ValueError):
    datasets.StreamingFilesDataset(
        os.path.join(self.get_temp_dir(), '*'), filetype='foo')
