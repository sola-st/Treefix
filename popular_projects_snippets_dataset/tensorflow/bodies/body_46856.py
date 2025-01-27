# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
"""AST representation."""
# The caller must adjust the context appropriately.
if self.has_subscript():
    exit(gast.Subscript(
        value=self.parent.ast(),
        slice=self.qn[-1].ast(),
        ctx=CallerMustSetThis))
if self.has_attr():
    exit(gast.Attribute(
        value=self.parent.ast(), attr=self.qn[-1], ctx=CallerMustSetThis))

base = self.qn[0]
if isinstance(base, str):
    exit(gast.Name(
        base, ctx=CallerMustSetThis, annotation=None, type_comment=None))
elif isinstance(base, Literal):
    exit(gast.Constant(base.value, kind=None))
else:
    assert False, ('the constructor should prevent types other than '
                   'str and Literal')
