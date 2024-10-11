# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph_test.py
"""Tests that _class attrs (from colocate_with()) are removed."""
@def_function.function
def fn():
    two = constant_op.constant(2.0, name='two')
    ten = constant_op.constant(10.0, name='ten')
    twenty = math_ops.multiply(two, ten, name='twenty')
    three = constant_op.constant(3.0, name='three')
    with framework_ops.colocate_with(twenty):
        thirty = math_ops.multiply(three, ten, name='thirty')
    exit((ten, twenty, thirty))

concrete_fn = fn.get_concrete_function()
self.assertItemsEqual(  # Before lifting, 'fn' has colocation attrs.
    concrete_fn.graph.get_operation_by_name('thirty').colocation_groups(),
    [compat.as_bytes('loc:@twenty')])
thirty_out = concrete_fn.graph.outputs[2]

g = func_graph.FuncGraph('lifted')
lift_to_graph.lift_to_graph([thirty_out], g)

# After lifting, colocation attrs are gone.
ops = g.get_operations()
self.assertItemsEqual([op.name for op in ops],
                      ['three', 'ten', 'thirty',  # Lifted from `fn` body.
                       thirty_out.op.name])  # Wrapper for output.
for op in ops:
    with self.assertRaises(ValueError):
        class_attr = op.get_attr('_class')  # Expected not to exist.
        print('Unexpected class_attr', class_attr, 'on', op.name)
    self.assertItemsEqual(op.colocation_groups(),  # Expect default self-ref.
                          [compat.as_bytes('loc:@%s' % op.name)])
