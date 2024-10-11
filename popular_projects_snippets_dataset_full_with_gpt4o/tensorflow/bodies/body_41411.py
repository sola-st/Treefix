# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
state = []

@polymorphic_function.function
def side_effecting_function():
    state.append(0)

side_effecting_function()
self.assertAllEqual(state, [0])

# The second invocation should call the graph function, which shouldn't
# trigger the list append.
side_effecting_function()
self.assertAllEqual(state, [0])

# Whereas calling the python function directly should create a side-effect.
side_effecting_function.python_function()
self.assertAllEqual(state, [0, 0])
