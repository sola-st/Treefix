# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
class HasVars(module.Module):

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None

    @polymorphic_function.function
    def make_x(self):
        if self.x is None:
            self.x = variables.Variable(1., name='v')

    def make_y(self):
        if self.y is None:
            self.y = variables.Variable(1., name='v')

    def make_z(self):
        if self.z is None:
            with ops.name_scope('z_scope', skip_on_eager=False):
                self.z = variables.Variable(1., name='z')

root = HasVars()
root.make_x()
root.make_y()
root.make_z()
self.assertEqual('v:0', root.x.name)
self.assertEqual('z_scope/z:0', root.z.name)
