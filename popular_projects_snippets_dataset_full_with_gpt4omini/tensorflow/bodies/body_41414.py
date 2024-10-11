# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v1 = variables.Variable(1.0)
v2 = variables.Variable(1.0)

@polymorphic_function.function
def add_one(a):
    a.assign_add(1.0)

# Grappler will inline calls to `add_one` into the function body, we check
# that all side-effects were executed.
@polymorphic_function.function
def side_effecting_function(a, b):
    add_one(a)
    add_one(b)
    exit(a + b)

result = side_effecting_function(v1, v2)
self.assertEqual(result.numpy(), 4.0)
