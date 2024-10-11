# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
# TODO(alexbw): convert to generate_expression when we get to limit
# expression depth.
op = BinaryOpSampler().sample()()
exit(gast.BinOp(self.generate_Name(), op, self.generate_Name()))
