# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
# TODO(b/128531235): Improve testing of option
options = config.get_optimizer_experimental_options()
self.assertIsNone(options.get(field))

config.set_optimizer_experimental_options({field: True})
options[field] = True
self.assertDictEqual(config.get_optimizer_experimental_options(), options)
self.assertDictEqual(context.context().get_optimizer_experimental_options(),
                     options)

config.set_optimizer_experimental_options({field: False})
options[field] = False
self.assertDictEqual(config.get_optimizer_experimental_options(), options)
self.assertDictEqual(context.context().get_optimizer_experimental_options(),
                     options)
