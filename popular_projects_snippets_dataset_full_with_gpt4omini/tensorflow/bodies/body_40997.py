# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'gpu' not in self.device.lower():
    self.skipTest('Only runs on GPU')

with ops.device('device:{}:0'.format(self.device)):
    writer = summary_ops_v2.create_file_writer(self.get_temp_dir())

    @polymorphic_function.function(jit_compile=True)
    def my_func_temp():
        with writer.as_default():
            summary_ops_v2.scalar('my_metric', 0.5, step=10)

    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                'Trying to access resource .*'):
        my_func_temp()
