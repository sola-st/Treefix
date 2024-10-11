# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.name_scope("inner", skip_on_eager=False), ops.init_scope():
    if context.executing_eagerly():
        # A trailing slash is always appended when eager execution is
        # enabled.
        self.assertEqual(context.context().scope_name, "inner/")
    else:
        self.assertEqual(ops.get_name_scope(), "inner")
