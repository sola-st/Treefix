# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
logits, logits_stacked, _ = pfor_input.input(0)
num_samples = pfor_input.unstacked_input(1)
seed = pfor_input.get_attr("seed")
seed2 = pfor_input.get_attr("seed2")
output_dtype = pfor_input.get_attr("output_dtype")
# TODO(b/222761732): Turn this warning back on when legacy RNGs are
#   deprecated.
# logging.warning(
#     "Note that Multinomial inside pfor op may not give same output as "
#     "inside a sequential loop.")

n = pfor_input.pfor.loop_len_vector[0]
if logits_stacked:
    flattened_logits = _flatten_first_two_dims(logits)
    samples = gen_random_ops.multinomial(
        flattened_logits,
        num_samples,
        seed=seed,
        seed2=seed2,
        output_dtype=output_dtype)
    stacked_samples = _unflatten_first_dim(samples, [n])
else:
    samples = gen_random_ops.multinomial(
        logits,
        num_samples * n,
        seed=seed,
        seed2=seed2,
        output_dtype=output_dtype)
    stacked_samples = array_ops.transpose(
        array_ops.reshape(samples, [-1, n, num_samples]), [1, 0, 2])

exit(wrap(stacked_samples, True))
