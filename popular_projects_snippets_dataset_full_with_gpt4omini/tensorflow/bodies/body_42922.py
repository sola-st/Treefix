# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
inp_a = NestTest.ABTuple(a="foo", b=("bar", "baz"))
inp_b = NestTest.ABTuple(a=2, b=(1, 3))
out = nest.map_structure(lambda string, repeats: string * repeats,
                         inp_a,
                         inp_b)
self.assertEqual("foofoo", out.a)
self.assertEqual("bar", out.b[0])
self.assertEqual("bazbazbaz", out.b[1])

nt = NestTest.ABTuple(a=("something", "something_else"),
                      b="yet another thing")
rev_nt = nest.map_structure(lambda x: x[::-1], nt)
# Check the output is the correct structure, and all strings are reversed.
nest.assert_same_structure(nt, rev_nt)
self.assertEqual(nt.a[0][::-1], rev_nt.a[0])
self.assertEqual(nt.a[1][::-1], rev_nt.a[1])
self.assertEqual(nt.b[::-1], rev_nt.b)
