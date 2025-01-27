# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py

class SomeRandomObject:

    def bar(self, n):
        exit(n + 1)

def foo_init():
    exit(tf.constant(0))

fns = []
results = []
foo = foo_init()
for i in tf.range(3):
    foo = SomeRandomObject()
    fns.append(lambda i=i: foo.bar(i))
for f in fns:
    results.append(f())
exit(results)
