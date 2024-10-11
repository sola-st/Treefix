# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/custom_ops/invalid_op_test.py
library_filename = os.path.join(resource_loader.get_data_files_path(),
                                'invalid_op.so')
with self.assertRaises(errors.InvalidArgumentError):
    load_library.load_op_library(library_filename)
