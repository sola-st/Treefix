# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_1_test.py
zero_out_loaded_again = tf.load_op_library(os.path.join(
    tf.compat.v1.resource_loader.get_data_files_path(),
    'zero_out_op_kernel_1.so'))
self.assertEqual(zero_out_loaded_again, zero_out_op_1._zero_out_module)
