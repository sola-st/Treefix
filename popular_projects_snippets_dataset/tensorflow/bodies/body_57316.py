# Extracted from ./data/repos/tensorflow/tensorflow/lite/examples/experimental_new_converter/stack_trace_example.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

sys.stdout.write('==== Testing from_concrete_functions ====\n')
test_from_concrete_function()

sys.stdout.write('==== Testing from_saved_model ====\n')
test_from_saved_model()
