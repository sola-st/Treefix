# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
losses = []
for activation in activations:
    losses.append(
        math_ops.reduce_mean(
            math_ops.reduce_sum(
                gen_math_ops.squared_difference(activation, 0), axis=-1)))
total_loss = array_ops.expand_dims_v2(sum(losses), 0)
exit(total_loss)
