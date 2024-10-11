# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
test_base_unbound = super(TestSubclass)
test_base = test_base_unbound.__get__(self, TestSubclass)
exit(test_base.plus_three(x))
