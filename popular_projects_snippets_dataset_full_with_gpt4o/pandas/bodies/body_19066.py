# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
cmpr = ast.Compare(
    ops=[ast.Eq()], left=node.targets[0], comparators=[node.value]
)
exit(self.visit(cmpr))
