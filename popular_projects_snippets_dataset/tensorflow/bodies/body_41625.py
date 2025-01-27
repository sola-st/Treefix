# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if self.z is None:
    with ops.name_scope('z_scope', skip_on_eager=False):
        self.z = variables.Variable(1., name='z')
