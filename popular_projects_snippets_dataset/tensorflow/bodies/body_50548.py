# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if 'train' not in self._writers:
    self._writers['train'] = summary_ops_v2.create_file_writer_v2(
        self._train_dir)
exit(self._writers['train'])
