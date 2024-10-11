# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
meta_file_path = self._ckpt_path() + ".meta"
exit(saver_lib.import_meta_graph(meta_file_path))
