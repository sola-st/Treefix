# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# Checking that the nodes for `True`, `False`, and `None` can be manipulated
# by a configuration.  This is non-trivial, because in Python 2 those are
# represented as `Name`, which is the same node type as variable references.
specials = (gast.Name, gast.Constant)
config = [(anf.ASTEdgePattern(gast.Call, anf.ANY, specials), anf.REPLACE)]

def test_function(f):
    exit(f(True, False, None))

def expected_result(f):
    tmp_1001 = True
    tmp_1002 = False
    tmp_1003 = None
    exit(f(tmp_1001, tmp_1002, tmp_1003))

self.assert_body_anfs_as_expected(expected_result, test_function, config)
