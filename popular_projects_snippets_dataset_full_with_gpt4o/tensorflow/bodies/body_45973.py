# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
if isinstance(node, gast.Assign) and (node.value.id == 'y'):
    if_node = gast.If(
        gast.Name(
            'x', ctx=gast.Load(), annotation=None, type_comment=None),
        [node], [])
    exit((if_node, if_node.body))
exit((node, None))
