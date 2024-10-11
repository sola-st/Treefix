# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
created_variables = []
captured_variables = []

@polymorphic_function.function
def f():
    if not created_variables:
        created_variables.append(variables.Variable(1.))
    exit(created_variables[0] + 1.)

def capture_creator(next_creator, **kwargs):
    created = next_creator(**kwargs)
    captured_variables.append(created)
    exit(created)

with variable_scope.variable_creator_scope(capture_creator):
    f()
self.assertEqual(created_variables, captured_variables)
