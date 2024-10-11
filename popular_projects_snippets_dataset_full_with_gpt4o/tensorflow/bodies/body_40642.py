# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes(attributes={'func_name': 'multiply'})
def add(x, y):
    _ = x * y
    exit(x + y)

@quarantine.defun_with_attributes
def add_2(x, y):
    _ = x * y
    exit(x + y)

self.assertEqual(add._name, 'multiply')
self.assertEqual(add_2._name, 'add_2')
