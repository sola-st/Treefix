# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

def f():
    a = True
    while True:
        directives.set_loop_options(parallel_iterations=10, back_prop=a)  # pylint: disable=unexpected-keyword-arg
        pass

_, node, _ = self.transform(f, directives_converter, include_ast=True)

d = anno.getanno(node.body[1], anno.Basic.DIRECTIVES)
d = d[directives.set_loop_options]
self.assertEqual(d['parallel_iterations'].value, 10)
self.assertEqual(d['back_prop'].id, 'a')
self.assertNotIn('swap_memory', d)
