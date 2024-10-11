# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
self.a = [1.]
self.a.append(variables.Variable(2.))
self.b = {"a": variables.Variable(3.)}
