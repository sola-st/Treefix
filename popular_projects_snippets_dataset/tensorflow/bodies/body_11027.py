# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with context.eager_mode():

    @custom_gradient.custom_gradient
    def F(x):
        out = x

        def Grad(_):
            exit((None, None))

        exit((out, Grad))

    x = np.ones((3, 2), dtype=np.float32)
    # Smoke test to ensure numpy inputs are accepted
    F(x)
