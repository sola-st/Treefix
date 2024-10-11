# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
inp_ab = ["a", "b"]
inp_abc = ["a", "b", "c"]
with self.assertRaisesWithLiteralMatch(  # pylint: disable=g-error-prone-assert-raises
    ValueError,
    nest._STRUCTURES_HAVE_MISMATCHING_LENGTHS.format(
        input_length=len(inp_ab),
        shallow_length=len(inp_abc))):
    nest.assert_shallow_structure(inp_abc, inp_ab)

inp_ab1 = [(1, 1), (2, 2)]
inp_ab2 = [[1, 1], [2, 2]]
with self.assertRaisesWithLiteralMatch(
    TypeError,
    nest._STRUCTURES_HAVE_MISMATCHING_TYPES.format(
        shallow_type=type(inp_ab2[0]),
        input_type=type(inp_ab1[0]))):
    nest.assert_shallow_structure(inp_ab2, inp_ab1)
nest.assert_shallow_structure(inp_ab2, inp_ab1, check_types=False)

inp_ab1 = {"a": (1, 1), "b": {"c": (2, 2)}}
inp_ab2 = {"a": (1, 1), "b": {"d": (2, 2)}}
with self.assertRaisesWithLiteralMatch(
    ValueError,
    nest._SHALLOW_TREE_HAS_INVALID_KEYS.format(["d"])):
    nest.assert_shallow_structure(inp_ab2, inp_ab1)

inp_ab = collections.OrderedDict([("a", 1), ("b", (2, 3))])
inp_ba = collections.OrderedDict([("b", (2, 3)), ("a", 1)])
nest.assert_shallow_structure(inp_ab, inp_ba)

# This assertion is expected to pass: two namedtuples with the same
# name and field names are considered to be identical.
inp_shallow = NestTest.SameNameab(1, 2)
inp_deep = NestTest.SameNameab2(1, [1, 2, 3])
nest.assert_shallow_structure(inp_shallow, inp_deep, check_types=False)
nest.assert_shallow_structure(inp_shallow, inp_deep, check_types=True)

# This assertion is expected to pass: two list-types with same number
# of fields are considered identical.
inp_shallow = _CustomList([1, 2])
inp_deep = [1, 2]
nest.assert_shallow_structure(inp_shallow, inp_deep, check_types=False)
nest.assert_shallow_structure(inp_shallow, inp_deep, check_types=True)

# This assertion is expected to pass: a VariableSpec with alias_id and
# a Variable are considered identical.
inp_shallow = resource_variable_ops.VariableSpec(None, alias_id=0)
inp_deep = resource_variable_ops.ResourceVariable(1.)
nest.assert_shallow_structure(inp_shallow, inp_deep,
                              expand_composites=False)
nest.assert_shallow_structure(inp_shallow, inp_deep,
                              expand_composites=True)
