# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_context_test.py
options = save_options.SaveOptions()
with self.assertRaisesRegex(ValueError, 'Already in a SaveContext'):
    with save_context.save_context(options):
        with save_context.save_context(options):
            pass
