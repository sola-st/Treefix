# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn(a):
        block
        return a
    """

class ShouldBeReplaced(object):
    pass

node = templates.replace(
    template,
    block=[
        gast.Assign(
            [
                gast.Name(
                    'a',
                    ctx=ShouldBeReplaced,
                    annotation=None,
                    type_comment=None)
            ],
            gast.BinOp(
                gast.Name(
                    'a',
                    ctx=ShouldBeReplaced,
                    annotation=None,
                    type_comment=None), gast.Add(),
                gast.Constant(1, kind=None)),
        ),
    ] * 2)[0]
result, _, _ = loader.load_ast(node)
self.assertEqual(3, result.test_fn(1))
