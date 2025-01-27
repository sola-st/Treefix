# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/pad/pad_ops_test.py
input_ = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)
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
self._assertOpAndComposite([input_], tf.raw_ops.MirrorPad,
                           ops_defs._composite_mirror_pad, kwargs_, kwargs)
# Make sure the translation and decomposition is correct
self._assertOpAndComposite([input_],
                           tf.function(gen_pad_ops.new_mirror_pad),
                           ops_defs._composite_mirror_pad, kwargs_)
