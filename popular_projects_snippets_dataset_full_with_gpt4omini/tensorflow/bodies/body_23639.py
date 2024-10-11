# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
d = {1: "a"}
nest.assert_same_structure(d, data_structures._DictWrapper(d.copy()))
