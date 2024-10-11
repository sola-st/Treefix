# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
n_draws = math_ops.cast(self.total_count, dtype=dtypes.int32)
k = self.event_shape_tensor()[0]
unnormalized_logits = array_ops.reshape(
    math_ops.log(random_ops.random_gamma(
        shape=[n],
        alpha=self.concentration,
        dtype=self.dtype,
        seed=seed)),
    shape=[-1, k])
draws = random_ops.multinomial(
    logits=unnormalized_logits,
    num_samples=n_draws,
    seed=distribution_util.gen_new_seed(seed, salt="dirichlet_multinomial"))
x = math_ops.reduce_sum(array_ops.one_hot(draws, depth=k), -2)
final_shape = array_ops.concat([[n], self.batch_shape_tensor(), [k]], 0)
x = array_ops.reshape(x, final_shape)
exit(math_ops.cast(x, self.dtype))
