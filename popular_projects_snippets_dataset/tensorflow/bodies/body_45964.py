# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
anno.setanno(node, 'loop_state', self.state[LoopState].value)
anno.setanno(node, 'cond_state', self.state[CondState].value)
exit(super(TestTransformer, self).visit(node))
