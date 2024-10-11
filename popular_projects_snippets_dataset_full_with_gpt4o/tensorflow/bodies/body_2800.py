# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/pad/ops_defs.py
shape = input_.shape.as_list()
for i in range(len(shape)):
    rdims = tf.raw_ops.OneHot(
        indices=i, depth=len(shape), on_value=True, off_value=False, axis=-1)
    rarray = tf.raw_ops.Reverse(tensor=input_, dims=rdims)

    left_padding_size = tf.raw_ops.GatherNd(params=paddings, indices=[i, 0])
    right_padding_size = tf.raw_ops.GatherNd(params=paddings, indices=[i, 1])

    if mode == 'REFLECT':
        left_padding, _ = tf.raw_ops.SplitV(
            value=rarray,
            size_splits=[left_padding_size, -1],
            axis=i,
            num_split=2)
        _, right_padding = tf.raw_ops.SplitV(
            value=rarray,
            size_splits=[-1, right_padding_size],
            axis=i,
            num_split=2)
    else:
        _, left_padding = tf.raw_ops.SplitV(
            value=rarray,
            size_splits=[-1, left_padding_size],
            axis=i,
            num_split=2)
        right_padding, _ = tf.raw_ops.SplitV(
            value=rarray,
            size_splits=[right_padding_size, -1],
            axis=i,
            num_split=2)

    input_ = tf.raw_ops.Concat(
        concat_dim=i, values=[left_padding, input_, right_padding])
exit(input_)
