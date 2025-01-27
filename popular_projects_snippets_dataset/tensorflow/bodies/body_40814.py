# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
functions_1 = []

def function_callback_1(f, name, graph, inputs, outputs):
    del name, graph, inputs, outputs
    functions_1.append(f)

functions_2 = []

def function_callback_2(f, name, graph, inputs, outputs):
    del name, graph, inputs, outputs
    functions_2.append(f)

@polymorphic_function.function
def plus_one(x):
    exit(x + 1)

try:
    quarantine.add_function_callback(function_callback_1)
    quarantine.add_function_callback(function_callback_2)
    self.assertAllClose(plus_one(numpy.array(3.0, dtype=numpy.float32)), 4.0)
    self.assertLen(functions_1, 1)
    self.assertLen(functions_2, 1)
    quarantine.remove_function_callback(function_callback_1)
    # The 1st callback should not be invokved after remove_function_callback()
    # is called.
    self.assertAllClose(plus_one(numpy.array(3.0, dtype=numpy.float64)), 4.0)
    self.assertLen(functions_1, 1)
    self.assertLen(functions_2, 2)
finally:
    quarantine.clear_function_callbacks()
