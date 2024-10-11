# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen_test.py
np.random.seed(0)
for _ in range(1000):
    node = codegen.generate_random_functiondef()
    fn = compiler.ast_to_object(node)
    self.assertIsNotNone(
        fn, 'Generated invalid AST that could not convert to source.')
