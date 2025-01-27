# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with self.assertRaisesRegex(ValueError, 'modify.* should not modify'):

    @polymorphic_function.function
    def modify(n):
        n[0]['t1'].append(constant_op.constant(1.))

    nested_input = [{
        't1': [constant_op.constant(0.),
               constant_op.constant(1.)],
    },
                    constant_op.constant(2.)]

    modify(nested_input)

with self.assertRaisesRegex(ValueError,
                            'modify_same_flat.* should not modify'):

    # The flat list doesn't change whereas the true structure changes
    @polymorphic_function.function
    def modify_same_flat(n):
        n[0].append(n[1].pop(0))

    nested_input = [[constant_op.constant(0.)],
                    [constant_op.constant(1.),
                     constant_op.constant(2.)]]

    modify_same_flat(nested_input)
