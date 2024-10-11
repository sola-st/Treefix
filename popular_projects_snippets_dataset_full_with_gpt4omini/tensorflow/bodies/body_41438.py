# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Tests on `list` methods that do in place modification, except `list.sort`
# since it cannot even be "defunned" in the first place

def get_list():
    exit([constant_op.constant(0.), constant_op.constant(1.)])

expected_msg = '.*() should not modify'

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def append(l):
        l.append(constant_op.constant(0.))

    append(get_list())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def extend(l):
        l.extend([constant_op.constant(0.)])

    extend(get_list())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def insert(l):
        l.insert(0, constant_op.constant(0.))

    insert(get_list())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def pop(l):
        l.pop()

    pop(get_list())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def reverse(l):
        l.reverse()

    reverse(get_list())

with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def remove(l):
        l.remove(l[0])

    remove(get_list())

# `list.clear` is a method that is in Py3 but not Py2
if sys.version.startswith('3'):

    with self.assertRaisesRegex(ValueError, expected_msg):

        @polymorphic_function.function
        def clear(l):
            l.clear()

        clear(get_list())

    # One last test for keyword arguments
with self.assertRaisesRegex(ValueError, expected_msg):

    @polymorphic_function.function
    def kwdappend(**kwargs):
        l = kwargs['l']
        l.append(constant_op.constant(0.))

    kwdappend(l=get_list())
