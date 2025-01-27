# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py

def dataset_fn():
    exit(dataset_ops.Dataset.list_files(path.join(self.tmp_dir, '*')))

self.assertDatasetProduces(
    dataset_fn(),
    expected_error=(errors.InvalidArgumentError,
                    'No files matched pattern'),
    requires_initialization=True)
