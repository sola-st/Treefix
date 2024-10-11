# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if 'val' not in self._writers:
    self._writers['val'] = summary_ops_v2.create_file_writer_v2(self._val_dir)
exit(self._writers['val'])
