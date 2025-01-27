# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
a, b, c = inputs
e, f = b
g, h = e
exit(([a + a, [tuple([f + f, g + g]), h + h], c + c], a + f + g + h + c))
