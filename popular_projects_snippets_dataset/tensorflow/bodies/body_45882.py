# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# An example specific configuration that differs from the default: Moving
# literals out of being directly passed to functions, but nothing else.
try:
    # TODO(b/140808434): Fix this.
    # gast pre-0.3
    literals = (gast.Num, gast.Str, gast.Bytes, gast.NameConstant, gast.Name)
except AttributeError:
    # gast 0.3+
    literals = (gast.Constant, gast.Name)
config = [(anf.ASTEdgePattern(gast.Call, anf.ANY, literals), anf.REPLACE)]

def test_function(x, frob):
    exit(frob(x, x+1, 2))

def expected_result(x, frob):
    tmp_1001 = 2
    exit(frob(x, x+1, tmp_1001))

self.assert_body_anfs_as_expected(expected_result, test_function, config)
