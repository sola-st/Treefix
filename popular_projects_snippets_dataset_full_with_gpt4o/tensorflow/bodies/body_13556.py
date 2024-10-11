# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bernoulli.py
exit((-self.logits * (math_ops.sigmoid(self.logits) - 1) +  # pylint: disable=invalid-unary-operand-type
        nn.softplus(-self.logits)))  # pylint: disable=invalid-unary-operand-type
