# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/shared_variable_creator_test.py

shared_variable_store = {}
num_devices = 3
creator_fns = []
for i in range(num_devices):
    creator_fn = shared_variable_creator.make_fn(shared_variable_store, i)
    creator_fns.append(creator_fn)

with variable_scope.variable_creator_scope(creator_fns[0]):
    v0 = variable_scope.variable(1.0, name="foo")

with variable_scope.variable_creator_scope(creator_fns[1]):
    v1 = variable_scope.variable(1.0, name="foo")

with variable_scope.variable_creator_scope(creator_fns[2]):
    v2 = variable_scope.variable(1.0, name="foo")

# v1 and v2 should be same as v0
self.assertIs(v1, v0)
self.assertIs(v2, v0)
