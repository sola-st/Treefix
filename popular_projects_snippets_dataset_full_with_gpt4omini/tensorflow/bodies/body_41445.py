# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def get_dict():
    exit({'t1': constant_op.constant(0.), 't2': constant_op.constant(1.)})

expected_msg = '.* should not modify'

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def clear(m):
        m.clear()

    clear(get_dict())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def pop(m):
        m.pop('t1')

    pop(get_dict())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def popitem(m):
        m.popitem()

    popitem(get_dict())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def update(m):
        m.update({'t1': constant_op.constant(3.)})

    update(get_dict())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def setdefault(m):
        m.setdefault('t3', constant_op.constant(3.))

    setdefault(get_dict())
