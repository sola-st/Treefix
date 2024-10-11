# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
del f, name, inputs

with graph.as_default():
    printer = logging_ops.print_v2(
        'hello', output_stream='file://' + file_name)
    outputs[0].op._add_control_input(printer)
