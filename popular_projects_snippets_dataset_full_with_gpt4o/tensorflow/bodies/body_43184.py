# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
checker1 = dispatch.make_type_checker(int)
checker2 = dispatch.make_type_checker(int)
self.assertIs(checker1, checker2)
