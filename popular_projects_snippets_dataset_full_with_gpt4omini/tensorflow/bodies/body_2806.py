# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/pad/pad_ops_test.py
input_ = tf.constant([[2, 1, 1, 2, 3, 3, 2], [2, 1, 1, 2, 3, 3, 2],
                      [5, 4, 4, 5, 6, 6, 5], [5, 4, 4, 5, 6, 6, 5]],
                     dtype=tf.float32)
paddings = tf.constant([[
    1,
    1,
], [2, 2]])
kwargs = {
    'input': input_,
    'paddings': paddings,
    'mode': mode,
}
kwargs_ = {
    'input_': input_,
    'paddings': paddings,
    'mode': mode,
}
# Make sure the composition python function is correct
self._assertOpAndComposite([input_], tf.raw_ops.MirrorPadGrad,
                           ops_defs._composite_mirror_pad_grad, kwargs_,
                           kwargs)
# Make sure the translation and decomposition is correct
self._assertOpAndComposite([input_],
                           tf.function(gen_pad_ops.new_mirror_pad_grad),
                           ops_defs._composite_mirror_pad_grad, kwargs_)
