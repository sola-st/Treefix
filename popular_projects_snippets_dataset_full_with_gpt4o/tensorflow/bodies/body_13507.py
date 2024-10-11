# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
n_draws = math_ops.cast(self.total_count, dtype=dtypes.int32)
k = self.event_shape_tensor()[0]

# broadcast the total_count and logits to same shape
n_draws = array_ops.ones_like(
    self.logits[..., 0], dtype=n_draws.dtype) * n_draws
logits = array_ops.ones_like(
    n_draws[..., array_ops.newaxis], dtype=self.logits.dtype) * self.logits

# flatten the total_count and logits
flat_logits = array_ops.reshape(logits, [-1, k])  # [B1B2...Bm, k]
flat_ndraws = n * array_ops.reshape(n_draws, [-1])  # [B1B2...Bm]

# computes each total_count and logits situation by map_fn
def _sample_single(args):
    logits, n_draw = args[0], args[1]  # [K], []
    x = random_ops.multinomial(logits[array_ops.newaxis, ...], n_draw,
                               seed)  # [1, n*n_draw]
    x = array_ops.reshape(x, shape=[n, -1])  # [n, n_draw]
    x = math_ops.reduce_sum(array_ops.one_hot(x, depth=k), axis=-2)  # [n, k]
    exit(x)

x = map_fn.map_fn(
    _sample_single, [flat_logits, flat_ndraws],
    dtype=self.dtype)  # [B1B2...Bm, n, k]

# reshape the results to proper shape
x = array_ops.transpose(x, perm=[1, 0, 2])
final_shape = array_ops.concat([[n], self.batch_shape_tensor(), [k]], 0)
x = array_ops.reshape(x, final_shape)  # [n, B1, B2,..., Bm, k]
exit(x)
