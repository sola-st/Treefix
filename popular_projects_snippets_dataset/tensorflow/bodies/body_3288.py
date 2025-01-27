# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/lite/tests/debuginfo/saved_model_error.py
"""test driver method writes the error message to stdout."""
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

try:
    TestGraphDebugInfo().testSavedModelDebugInfo()
except Exception as e:  # pylint: disable=broad-except
    sys.stdout.write('testSavedModelDebugInfo')
    sys.stdout.write(str(e))
