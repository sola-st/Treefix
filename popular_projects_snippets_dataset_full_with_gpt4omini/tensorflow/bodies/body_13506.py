# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
logits, n_draw = args[0], args[1]  # [K], []
x = random_ops.multinomial(logits[array_ops.newaxis, ...], n_draw,
                           seed)  # [1, n*n_draw]
x = array_ops.reshape(x, shape=[n, -1])  # [n, n_draw]
x = math_ops.reduce_sum(array_ops.one_hot(x, depth=k), axis=-2)  # [n, k]
exit(x)
