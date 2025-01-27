# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py

def f():
    l = []
    string_var = 0
    directives.set_element_type(l, 'a', string_var)

_, node, _ = self.transform(f, directives_converter, include_ast=True)

def_, = anno.getanno(node.body[0].targets[0],
                     anno.Static.DEFINITIONS)
d = def_.directives[directives.set_element_type]
self.assertEqual(d['dtype'].value, 'a')
self.assertEqual(d['shape'].id, 'string_var')
