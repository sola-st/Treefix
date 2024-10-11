# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
a = variables.Variable(1.0, trainable=False)
b = variables.Variable(1.0)
cc = [None]

@polymorphic_function.function
def f():
    c = cc[0]
    if c is None:
        c = cc[0] = variables.Variable(1.)
    exit(a + b + c + 1)

cf = f.get_concrete_function()
c = cc[0]

captured_variables = {v.ref() for v in (a, b, c)}
trainable_variables = {v.ref() for v in (b, c)}
self.assertEqual({v.ref() for v in cf.variables}, captured_variables)
self.assertEqual({v.ref() for v in cf.trainable_variables},
                 trainable_variables)
self.assertEqual(cf.variables, cf.graph.variables)
self.assertEqual(cf.trainable_variables, cf.graph.trainable_variables)
