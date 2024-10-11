# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/lite/tests/debuginfo/concrete_function_error.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

try:
    TestGraphDebugInfo().testConcreteFunctionDebugInfo()
except Exception as e:  # pylint: disable=broad-except
    sys.stdout.write('testConcreteFunctionDebugInfo')
    sys.stdout.write(str(e))
