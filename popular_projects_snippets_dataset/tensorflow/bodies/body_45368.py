# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py

def f(x):
    while x > 0:
        x -= 1
        if x % 2 == 0:
            break

_, node, ctx = self.transform(f, (), include_ast=True)
fake_annotation = object()
anno.setanno(node.body[0], anno.Basic.DIRECTIVES, fake_annotation)
node = break_statements.transform(node, ctx)

self.assertIs(
    anno.getanno(node.body[1], anno.Basic.DIRECTIVES), fake_annotation)
