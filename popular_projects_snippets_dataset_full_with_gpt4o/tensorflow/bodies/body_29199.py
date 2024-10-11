# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
inp_ab = ("a", "b")
inp_abc = ("a", "b", "c")
expected_message = (
    "The two structures don't have the same sequence length. Input "
    "structure has length 2, while shallow structure has length 3.")
with self.assertRaisesRegex(ValueError, expected_message):
    nest.assert_shallow_structure(inp_abc, inp_ab)

inp_ab1 = ((1, 1), (2, 2))
inp_ab2 = {"a": (1, 1), "b": (2, 2)}
expected_message = (
    "The two structures don't have the same sequence type. Input structure "
    "has type 'tuple', while shallow structure has type "
    "'dict'.")
with self.assertRaisesRegex(TypeError, expected_message):
    nest.assert_shallow_structure(inp_ab2, inp_ab1)
nest.assert_shallow_structure(inp_ab2, inp_ab1, check_types=False)

inp_ab1 = {"a": (1, 1), "b": {"c": (2, 2)}}
inp_ab2 = {"a": (1, 1), "b": {"d": (2, 2)}}
expected_message = (
    r"The two structures don't have the same keys. Input "
    r"structure has keys \['c'\], while shallow structure has "
    r"keys \['d'\].")
with self.assertRaisesRegex(ValueError, expected_message):
    nest.assert_shallow_structure(inp_ab2, inp_ab1)

inp_ab = collections.OrderedDict([("a", 1), ("b", (2, 3))])
inp_ba = collections.OrderedDict([("b", (2, 3)), ("a", 1)])
nest.assert_shallow_structure(inp_ab, inp_ba)
