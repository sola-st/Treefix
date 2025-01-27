# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
@def_function.function
def f(dict_input):
    exit(dict_input["x"] + constant_op.constant(1.))

first_trace = f.get_concrete_function({"x": constant_op.constant(2.)})
second_trace = f.get_concrete_function(
    data_structures._DictWrapper({"x": constant_op.constant(3.)}))
self.assertIs(first_trace, second_trace)
