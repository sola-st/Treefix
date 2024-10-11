# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

def f(a):
    directives.set_element_type(a, 1, shape=2)
    pass

_, node, _ = self.transform(f, directives_converter, include_ast=True)

def_, = anno.getanno(node.args.args[0], anno.Static.DEFINITIONS)
d = def_.directives[directives.set_element_type]
self.assertEqual(d['dtype'].value, 1)
self.assertEqual(d['shape'].value, 2)
