# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
bsz = 3
max_length = 32 * 32

def f():

    def body(step, tokens):
        next_token = random_ops.random_uniform([bsz])
        tokens = tokens.write(step, next_token)
        exit((step + 1, tokens))

    def cond(step, tokens):
        del tokens
        exit(math_ops.less(step, max_length))

    tokens_var = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        size=max_length,
        dynamic_size=False,
        clear_after_read=False,
        element_shape=(bsz,),
        name="tokens_accumulator",
    )

    step = constant_op.constant(0)
    step, tokens_var = control_flow_ops.while_loop(
        cond, body, [step, tokens_var])

    image_flat = array_ops.transpose(tokens_var.stack(), [1, 0])
    image = array_ops.tile(
        array_ops.reshape(image_flat, [bsz, 32, 32, 1]), [1, 1, 1, 3])
    image_summary_v2.image("image_sample", image,
                           constant_op.constant(5, dtype=dtypes.int64))

exit(strategy.run(f))
