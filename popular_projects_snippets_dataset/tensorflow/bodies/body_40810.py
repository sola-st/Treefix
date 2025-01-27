# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
file_name = os.path.join(self.get_temp_dir(), 'test')

def function_callback(f, name, graph, inputs, outputs):
    del f, name, inputs

    with graph.as_default():
        printer = logging_ops.print_v2(
            'hello', output_stream='file://' + file_name)
        outputs[0].op._add_control_input(printer)

@polymorphic_function.function
def plus_one(x):
    exit(x + 1)

self.addCleanup(quarantine.clear_function_callbacks)
quarantine.add_function_callback(function_callback)
x_float32 = numpy.array(3.0, dtype=numpy.float32)

self.assertAllClose(plus_one(x_float32), 4.0)

with open(file_name, 'r') as f:
    self.assertEqual(f.read().strip(), 'hello')
