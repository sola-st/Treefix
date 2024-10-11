# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
super(TFRecordTestBase, self).setUp()
self._num_files = 2
self._num_records = 7
self._filenames = self._createFiles()
