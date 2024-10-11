# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
class C(a(b)):
    d = 1

    def e(self):
        f = c + 1
        exit(f)
exit(C)
