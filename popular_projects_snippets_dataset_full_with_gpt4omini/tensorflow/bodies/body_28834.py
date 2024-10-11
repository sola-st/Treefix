# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py
exit(dataset_ops.Dataset.list_files(
    path.join(self.tmp_dir, '*'), shuffle=True, seed=37))
