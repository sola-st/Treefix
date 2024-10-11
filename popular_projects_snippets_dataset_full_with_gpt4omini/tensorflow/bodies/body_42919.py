# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
structure1 = (((1, 2), 3), 4, (5, 6))
structure2 = ((("foo1", "foo2"), "foo3"), "foo4", ("foo5", "foo6"))
structure_different_num_elements = ("spam", "eggs")
structure_different_nesting = (((1, 2), 3), 4, 5, (6,))
nest.assert_same_structure(structure1, structure2)
nest.assert_same_structure("abc", 1.0)
nest.assert_same_structure("abc", np.array([0, 1]))
nest.assert_same_structure("abc", constant_op.constant([0, 1]))

with self.assertRaisesRegex(
    ValueError,
    ("The two structures don't have the same nested structure\\.\n\n"
     "First structure:.*?\n\n"
     "Second structure:.*\n\n"
     "More specifically: Substructure "
     r'"type=tuple str=\(\(1, 2\), 3\)" is a sequence, while '
     'substructure "type=str str=spam" is not\n'
     "Entire first structure:\n"
     r"\(\(\(\., \.\), \.\), \., \(\., \.\)\)\n"
     "Entire second structure:\n"
     r"\(\., \.\)")):
    nest.assert_same_structure(structure1, structure_different_num_elements)

with self.assertRaisesRegex(
    ValueError,
    ("The two structures don't have the same nested structure\\.\n\n"
     "First structure:.*?\n\n"
     "Second structure:.*\n\n"
     r'More specifically: Substructure "type=list str=\[0, 1\]" '
     r'is a sequence, while substructure "type=ndarray str=\[0 1\]" '
     "is not")):
    nest.assert_same_structure([0, 1], np.array([0, 1]))

with self.assertRaisesRegex(
    ValueError,
    ("The two structures don't have the same nested structure\\.\n\n"
     "First structure:.*?\n\n"
     "Second structure:.*\n\n"
     r'More specifically: Substructure "type=list str=\[0, 1\]" '
     'is a sequence, while substructure "type=int str=0" '
     "is not")):
    nest.assert_same_structure(0, [0, 1])

self.assertRaises(TypeError, nest.assert_same_structure, (0, 1), [0, 1])

with self.assertRaisesRegex(ValueError,
                            ("don't have the same nested structure\\.\n\n"
                             "First structure: .*?\n\nSecond structure: ")):
    nest.assert_same_structure(structure1, structure_different_nesting)

self.assertRaises(TypeError, nest.assert_same_structure, (0, 1),
                  NestTest.Named0ab("a", "b"))

nest.assert_same_structure(NestTest.Named0ab(3, 4),
                           NestTest.Named0ab("a", "b"))

self.assertRaises(TypeError, nest.assert_same_structure,
                  NestTest.Named0ab(3, 4), NestTest.Named1ab(3, 4))

with self.assertRaisesRegex(ValueError,
                            ("don't have the same nested structure\\.\n\n"
                             "First structure: .*?\n\nSecond structure: ")):
    nest.assert_same_structure(NestTest.Named0ab(3, 4),
                               NestTest.Named0ab([3], 4))

with self.assertRaisesRegex(ValueError,
                            ("don't have the same nested structure\\.\n\n"
                             "First structure: .*?\n\nSecond structure: ")):
    nest.assert_same_structure([[3], 4], [3, [4]])

structure1_list = [[[1, 2], 3], 4, [5, 6]]
with self.assertRaisesRegex(TypeError, "don't have the same sequence type"):
    nest.assert_same_structure(structure1, structure1_list)
nest.assert_same_structure(structure1, structure2, check_types=False)
nest.assert_same_structure(structure1, structure1_list, check_types=False)

with self.assertRaisesRegex(ValueError, "don't have the same set of keys"):
    nest.assert_same_structure({"a": 1}, {"b": 1})

nest.assert_same_structure(NestTest.SameNameab(0, 1),
                           NestTest.SameNameab2(2, 3))

# This assertion is expected to pass: two namedtuples with the same
# name and field names are considered to be identical.
nest.assert_same_structure(
    NestTest.SameNameab(NestTest.SameName1xy(0, 1), 2),
    NestTest.SameNameab2(NestTest.SameName1xy2(2, 3), 4))

expected_message = "The two structures don't have the same.*"
with self.assertRaisesRegex(ValueError, expected_message):
    nest.assert_same_structure(
        NestTest.SameNameab(0, NestTest.SameNameab2(1, 2)),
        NestTest.SameNameab2(NestTest.SameNameab(0, 1), 2))

self.assertRaises(TypeError, nest.assert_same_structure,
                  NestTest.SameNameab(0, 1), NestTest.NotSameName(2, 3))

self.assertRaises(TypeError, nest.assert_same_structure,
                  NestTest.SameNameab(0, 1), NestTest.SameNamexy(2, 3))

self.assertRaises(TypeError, nest.assert_same_structure,
                  NestTest.SameNameab(0, 1), NestTest.SameNamedType1(2, 3))
