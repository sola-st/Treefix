# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
var = variables.Variable(initial_value=0)

@def_function.function
def func():
    with ops.device('/job:localhost/task:0'):
        read = var.read_value()
    exit(read + 1)

with ops.device('/job:worker/task:0'):
    self.assertAllEqual(func(), 1)
