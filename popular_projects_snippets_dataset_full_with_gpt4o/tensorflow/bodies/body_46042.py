# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
operand = self.generate_Name()
op = UnaryOpSampler().sample()()
exit(gast.UnaryOp(op, operand))
