# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
# In Python 3.9, "abstract methods" become "abstract method"
with self.assertRaisesRegex(TypeError,
                            ("Can't instantiate abstract class Bijector "
                             "with abstract methods? __init__")):
    bijector.Bijector()  # pylint: disable=abstract-class-instantiated
