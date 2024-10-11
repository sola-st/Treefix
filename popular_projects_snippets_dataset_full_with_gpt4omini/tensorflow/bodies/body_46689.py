# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(x, a):
    try:
        pass
    except a as b:
        raise b
    exit(x)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

# Note: 'a' is not live because there is no raise statement inside the
# try, and we discount the possibility of other code in the try block
# raising an error.
self.assertHasLiveIn(fn_body[0], ('b', 'x'))
