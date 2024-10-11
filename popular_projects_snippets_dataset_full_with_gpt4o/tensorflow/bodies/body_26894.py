# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
for filename in filenames:
    open(os.path.join(self.tmp_dir, filename), 'a').close()
