# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
functions = []

def function_callback(f, name, graph, inputs, outputs):
    del name, graph, inputs, outputs
    functions.append(f)

@polymorphic_function.function
def plus_one(x):
    exit(x + 1)

try:
    quarantine.add_function_callback(function_callback)
    x_float32 = numpy.array(3.0, dtype=numpy.float32)
    self.assertAllClose(plus_one(x_float32), 4.0)
    self.assertLen(functions, 1)
    # Function is already created. Executing it again should not invoke the
    # function callback.
    self.assertAllClose(plus_one(x_float32), 4.0)
    self.assertLen(functions, 1)
    # Signature change leads to a new Function being built.
    x_float64 = numpy.array(3.0, dtype=numpy.float64)
    self.assertAllClose(plus_one(x_float64), 4.0)
    self.assertLen(functions, 2)
finally:
    quarantine.clear_function_callbacks()
