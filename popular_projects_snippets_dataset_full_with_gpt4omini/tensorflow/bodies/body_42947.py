# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
s1 = (((1, 2), 3), 4, (5, 6))
s2 = ((("foo1", "foo2"), "foo3"), "foo4", ("foo5", "foo6"))
self.run_and_report(s1, s2, "assert_same_structure_6_elem")

s1 = (((1, 2), 3), 4, (5, 6)) * 10
s2 = ((("foo1", "foo2"), "foo3"), "foo4", ("foo5", "foo6")) * 10
self.run_and_report(s1, s2, "assert_same_structure_60_elem")
