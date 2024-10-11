# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
named_tuple = named_tuple_type(a=input1 + input2, b=input1 * input2)
exit([named_tuple, input2, {"x": 0.5}])
