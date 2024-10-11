# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
node = gast.If(
    test=gast.Constant(1, kind=None),
    body=[
        gast.Assign(
            targets=[
                gast.Name(
                    'a',
                    ctx=gast.Store(),
                    annotation=None,
                    type_comment=None)
            ],
            value=gast.Name(
                'b', ctx=gast.Load(), annotation=None, type_comment=None))
    ],
    orelse=[
        gast.Assign(
            targets=[
                gast.Name(
                    'a',
                    ctx=gast.Store(),
                    annotation=None,
                    type_comment=None)
            ],
            value=gast.Constant('c', kind=None))
    ])

source = parser.unparse(node, indentation='  ')
self.assertEqual(
    textwrap.dedent("""
            # coding=utf-8
            if 1:
                a = b
            else:
                a = 'c'
        """).strip(), source.strip())
