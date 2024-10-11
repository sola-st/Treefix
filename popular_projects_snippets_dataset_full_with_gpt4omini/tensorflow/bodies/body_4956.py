# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py

class Model(module.Module):

    def __init__(self):
        super().__init__()
        variables = [
            variables_lib.Variable([0]),
            variables_lib.Variable([1]),
        ]
        self.w = sharded_variable.ShardedVariable(variables)

model = Model()

self.assertLen(model.variables, 2)
self.assertEqual(model.variables[0], [0])
self.assertEqual(model.variables[1], [1])
self.assertAllEqual(model.variables, model.trainable_variables)

self.assertLen(model._trackable_children(), 1)
self.assertIs(model._trackable_children().popitem()[1], model.w)
