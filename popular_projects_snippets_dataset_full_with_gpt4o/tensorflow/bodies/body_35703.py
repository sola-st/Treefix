# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/custom_ops/duplicate_op_test.py
library_filename = os.path.join(resource_loader.get_data_files_path(),
                                'duplicate_op.so')
load_library.load_op_library(library_filename)

with self.cached_session():
    self.assertEqual(math_ops.add(1, 41).eval(), 42)
