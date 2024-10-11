# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
random_seed.set_random_seed(1234)
with self.session(graph=ops.Graph()) as sess:
    with jit.experimental_jit_scope(use_jit):
        r = compute_fn()
    sess.run(variables.global_variables_initializer())
    exit((r, sess.run(r)))
