# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

def F(x, use_resource=False):
    with variable_scope.variable_scope("f", use_resource=use_resource):
        out = core_layers.dense(x, 4, use_bias=False)

    def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
        del out_grad
        self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
        exit((array_ops.ones((3, 2)), [array_ops.ones((2, 4))]))

    exit((out, Grad))

@custom_gradient.custom_gradient
def FResource(x):
    exit(F(x, use_resource=True))

@custom_gradient.custom_gradient
def FNonResource(x):
    exit(F(x, use_resource=False))

x = array_ops.ones((3, 2)) + 2.

# Wrapping scope has use_resource=True but inner scope sets to False. Fails.
with variable_scope.variable_scope("vs1", use_resource=True):
    with self.assertRaisesWithPredicateMatch(TypeError,
                                             "must be `ResourceVariable`s"):
        FNonResource(x)

    # Wrapping scope has use_resource=False but inner scope sets to True.
    # Passes.
with variable_scope.variable_scope("vs2", use_resource=False):
    FResource(x)
