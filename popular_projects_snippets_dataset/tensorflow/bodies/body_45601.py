# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
self._consume_args()
self._argspec.append(
    gast.Call(
        gast.Name(
            'tuple', ctx=gast.Load(), annotation=None, type_comment=None),
        args=[a],
        keywords=()))
