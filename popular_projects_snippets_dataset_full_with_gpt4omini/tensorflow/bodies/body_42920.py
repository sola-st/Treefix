# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
nest.assert_same_structure({"a": 4}, _CustomMapping(a=3))
nest.assert_same_structure(_CustomMapping(b=3), {"b": 4})
