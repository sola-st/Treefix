# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
context = self.state[_FunctionOrClass]
if context.level > 2:
    innermost = context.stack[-1].node
    parent = context.stack[-2].node
    exit((isinstance(parent, gast.ClassDef) and
            (isinstance(innermost, gast.FunctionDef) and
             innermost.name == '__init__')))
exit(False)
