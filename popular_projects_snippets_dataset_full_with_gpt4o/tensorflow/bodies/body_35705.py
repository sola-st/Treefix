# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/custom_ops/ackermann_test.py
library_filename = os.path.join(resource_loader.get_data_files_path(),
                                'ackermann_op.so')
ackermann = load_library.load_op_library(library_filename)

with self.cached_session():
    self.assertEqual(ackermann.ackermann().eval(), b'A(m, 0) == A(m-1, 1)')
