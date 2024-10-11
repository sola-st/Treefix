# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that unsupported operations are detected."""
context = self.create_test_xla_compile_context()
context.Enter()
dummy_tensor = constant_op.constant(1.1)
audio_summary = summary.audio('audio_summary', dummy_tensor, 0.5)
histogram_summary = summary.histogram('histogram_summary', dummy_tensor)
image_summary = summary.image('image_summary', dummy_tensor)
scalar_summary = summary.scalar('scalar_summary', dummy_tensor)
tensor_summary = summary.tensor_summary('tensor_summary', dummy_tensor)
summary.merge(
    [
        audio_summary, histogram_summary, image_summary, scalar_summary,
        tensor_summary
    ],
    name='merge_summary')
logging_ops.Print(dummy_tensor, [dummy_tensor], name='print_op')
context.Exit()

unsupported_ops_names = [op.name for op in context._unsupported_ops]
self.assertEqual(unsupported_ops_names, [
    u'audio_summary', u'histogram_summary', u'image_summary',
    u'scalar_summary', u'tensor_summary', u'merge_summary/merge_summary',
    u'print_op'
])
