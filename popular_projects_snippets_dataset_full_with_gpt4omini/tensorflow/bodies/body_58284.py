# Extracted from ./data/repos/tensorflow/tensorflow/cc/experimental/libtf/tests/generate_testdata.py
self.arr1 = [1.]
self.const_arr = [constant_op.constant(1.)]
self.var_arr = [variables.Variable(1.), variables.Variable(2.)]
self.dict1 = {"a": 1.}
self.var_dict = {"a": variables.Variable(1.), "b": variables.Variable(2.)}
