# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
# Named tuples.
ab_tuple = collections.namedtuple("ab_tuple", "a, b")
op_tuple = collections.namedtuple("op_tuple", "add, mul")
inp_val = ab_tuple(a=2, b=3)
inp_ops = ab_tuple(a=op_tuple(add=1, mul=2), b=op_tuple(add=2, mul=3))
out = nest.map_structure_up_to(
    inp_val, lambda val, ops: (val + ops.add) * ops.mul, inp_val, inp_ops)
self.assertEqual(out.a, 6)
self.assertEqual(out.b, 15)

# Lists.
data_list = [[2, 4, 6, 8], [[1, 3, 5, 7, 9], [3, 5, 7]]]
name_list = ["evens", ["odds", "primes"]]
out = nest.map_structure_up_to(
    name_list, lambda name, sec: "first_{}_{}".format(len(sec), name),
    name_list, data_list)
self.assertEqual(out, ["first_4_evens", ["first_5_odds", "first_3_primes"]])

# Dicts.
inp_val = dict(a=2, b=3)
inp_ops = dict(a=dict(add=1, mul=2), b=dict(add=2, mul=3))
out = nest.map_structure_up_to(
    inp_val,
    lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)
self.assertEqual(out["a"], 6)
self.assertEqual(out["b"], 15)

# Non-equal dicts.
inp_val = dict(a=2, b=3)
inp_ops = dict(a=dict(add=1, mul=2), c=dict(add=2, mul=3))
with self.assertRaisesWithLiteralMatch(
    ValueError,
    nest._SHALLOW_TREE_HAS_INVALID_KEYS.format(["b"])):
    nest.map_structure_up_to(
        inp_val,
        lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)

# Dict+custom mapping.
inp_val = dict(a=2, b=3)
inp_ops = _CustomMapping(a=dict(add=1, mul=2), b=dict(add=2, mul=3))
out = nest.map_structure_up_to(
    inp_val,
    lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)
self.assertEqual(out["a"], 6)
self.assertEqual(out["b"], 15)

# Non-equal dict/mapping.
inp_val = dict(a=2, b=3)
inp_ops = _CustomMapping(a=dict(add=1, mul=2), c=dict(add=2, mul=3))
with self.assertRaisesWithLiteralMatch(
    ValueError,
    nest._SHALLOW_TREE_HAS_INVALID_KEYS.format(["b"])):
    nest.map_structure_up_to(
        inp_val,
        lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)
