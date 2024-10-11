# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
structure1 = (((1, 2), 3), 4, (5, 6))
structure2 = ((("foo1", "foo2"), "foo3"), "foo4", ("foo5", "foo6"))
structure_different_num_elements = ("spam", "eggs")
structure_different_nesting = (((1, 2), 3), 4, 5, (6,))
structure_dictionary = {"foo": 2, "bar": 4, "baz": {"foo": 5, "bar": 6}}
structure_dictionary_diff_nested = {
    "foo": 2,
    "bar": 4,
    "baz": {
        "foo": 5,
        "baz": 6
    }
}
nest.assert_same_structure(structure1, structure2)
nest.assert_same_structure("abc", 1.0)
nest.assert_same_structure("abc", np.array([0, 1]))
nest.assert_same_structure("abc", constant_op.constant([0, 1]))

with self.assertRaisesRegex(ValueError,
                            "don't have the same nested structure"):
    nest.assert_same_structure(structure1, structure_different_num_elements)

with self.assertRaisesRegex(ValueError,
                            "don't have the same nested structure"):
    nest.assert_same_structure((0, 1), np.array([0, 1]))

with self.assertRaisesRegex(ValueError,
                            "don't have the same nested structure"):
    nest.assert_same_structure(0, (0, 1))

with self.assertRaisesRegex(ValueError,
                            "don't have the same nested structure"):
    nest.assert_same_structure(structure1, structure_different_nesting)

named_type_0 = collections.namedtuple("named_0", ("a", "b"))
named_type_1 = collections.namedtuple("named_1", ("a", "b"))
self.assertRaises(TypeError, nest.assert_same_structure, (0, 1),
                  named_type_0("a", "b"))

nest.assert_same_structure(named_type_0(3, 4), named_type_0("a", "b"))

self.assertRaises(TypeError, nest.assert_same_structure,
                  named_type_0(3, 4), named_type_1(3, 4))

with self.assertRaisesRegex(ValueError,
                            "don't have the same nested structure"):
    nest.assert_same_structure(named_type_0(3, 4), named_type_0((3,), 4))

with self.assertRaisesRegex(ValueError,
                            "don't have the same nested structure"):
    nest.assert_same_structure(((3,), 4), (3, (4,)))

structure1_list = {"a": ((1, 2), 3), "b": 4, "c": (5, 6)}
structure2_list = {"a": ((1, 2), 3), "b": 4, "d": (5, 6)}
with self.assertRaisesRegex(TypeError, "don't have the same sequence type"):
    nest.assert_same_structure(structure1, structure1_list)
nest.assert_same_structure(structure1, structure2, check_types=False)
nest.assert_same_structure(structure1, structure1_list, check_types=False)
with self.assertRaisesRegex(ValueError, "don't have the same set of keys"):
    nest.assert_same_structure(structure1_list, structure2_list)
with self.assertRaisesRegex(ValueError, "don't have the same set of keys"):
    nest.assert_same_structure(structure_dictionary,
                               structure_dictionary_diff_nested)
nest.assert_same_structure(
    structure_dictionary,
    structure_dictionary_diff_nested,
    check_types=False)
nest.assert_same_structure(
    structure1_list, structure2_list, check_types=False)
