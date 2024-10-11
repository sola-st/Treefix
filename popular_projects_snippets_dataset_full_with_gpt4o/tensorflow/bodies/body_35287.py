# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
## The parameters have a single batch dimension, and the event has two.

# param shape is [3 x 4], where 4 is the number of bins (non-batch dim).
cat_params_py = [
    [0.2, 0.15, 0.35, 0.3],
    [0.1, 0.05, 0.68, 0.17],
    [0.1, 0.05, 0.68, 0.17]
]

# event shape = [5, 3], both are "batch" dimensions.
disc_event_py = [
    [0, 1, 2],
    [1, 2, 3],
    [0, 0, 0],
    [1, 1, 1],
    [2, 1, 0]
]

# shape is [3]
normal_params_py = [
    -10.0,
    120.0,
    50.0
]

# shape is [5, 3]
real_event_py = [
    [-1.0, 0.0, 1.0],
    [100.0, 101, -50],
    [90, 90, 90],
    [-4, -400, 20.0],
    [0.0, 0.0, 0.0]
]

cat_params_tf = array_ops.constant(cat_params_py)
disc_event_tf = array_ops.constant(disc_event_py)
cat = categorical.Categorical(probs=cat_params_tf)

normal_params_tf = array_ops.constant(normal_params_py)
real_event_tf = array_ops.constant(real_event_py)
norm = normal.Normal(loc=normal_params_tf, scale=1.0)

# Check that normal and categorical have the same broadcasting behaviour.
to_run = {
    "cat_prob": cat.prob(disc_event_tf),
    "cat_log_prob": cat.log_prob(disc_event_tf),
    "cat_cdf": cat.cdf(disc_event_tf),
    "cat_log_cdf": cat.log_cdf(disc_event_tf),
    "norm_prob": norm.prob(real_event_tf),
    "norm_log_prob": norm.log_prob(real_event_tf),
    "norm_cdf": norm.cdf(real_event_tf),
    "norm_log_cdf": norm.log_cdf(real_event_tf),
}

with self.cached_session() as sess:
    run_result = self.evaluate(to_run)

self.assertAllEqual(run_result["cat_prob"].shape,
                    run_result["norm_prob"].shape)
self.assertAllEqual(run_result["cat_log_prob"].shape,
                    run_result["norm_log_prob"].shape)
self.assertAllEqual(run_result["cat_cdf"].shape,
                    run_result["norm_cdf"].shape)
self.assertAllEqual(run_result["cat_log_cdf"].shape,
                    run_result["norm_log_cdf"].shape)
