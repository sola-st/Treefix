# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/loader_test.py
node = gast.FunctionDef(
    name='f',
    args=gast.arguments(
        args=[
            gast.Name(
                'a', ctx=gast.Param(), annotation=None, type_comment=None)
        ],
        posonlyargs=[],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]),
    body=[
        gast.Return(
            gast.BinOp(
                op=gast.Add(),
                left=gast.Name(
                    'a',
                    ctx=gast.Load(),
                    annotation=None,
                    type_comment=None),
                right=gast.Constant(1, kind=None)))
    ],
    decorator_list=[],
    returns=None,
    type_comment=None)

module, source, _ = loader.load_ast(node)

expected_node_src = """
      # coding=utf-8
      def f(a):
          return (a + 1)
    """
expected_node_src = textwrap.dedent(expected_node_src)

self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)

self.assertEqual(2, module.f(1))
with open(module.__file__, 'r') as temp_output:
    self.assertAstMatches(node, temp_output.read())
