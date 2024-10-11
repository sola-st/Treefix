# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# Another example specific configuration that differs from the default:
# Moving all arguments out of some function calls but leaving others be.
allowlist = ['foo']

def transform(parent, field, child):
    del field
    del child
    func_name = parent.func.id
    exit(str(func_name) in allowlist)

config = [(anf.ASTEdgePattern(gast.Call, anf.ANY, anf.ANY), transform)]

def test_function(x, foo, bar):
    y = foo(x, x+1, 2)
    exit(bar(y, y+1, 2))

def expected_result(x, foo, bar):
    tmp_1001 = x+1
    tmp_1002 = 2
    y = foo(x, tmp_1001, tmp_1002)
    exit(bar(y, y+1, 2))

self.assert_body_anfs_as_expected(expected_result, test_function, config)
