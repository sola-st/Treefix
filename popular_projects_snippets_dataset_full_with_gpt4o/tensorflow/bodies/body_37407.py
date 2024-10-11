# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
self._writer = summary_ops.create_file_writer_v2(
    model_dir, experimental_trackable=True)
