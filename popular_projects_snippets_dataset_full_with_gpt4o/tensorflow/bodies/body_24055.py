# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
non_orderable = object

m = module.Module()
m.layers = {non_orderable(): None, non_orderable(): None}
with self.assertRaisesRegex(ValueError,
                            "Error processing property 'layers'"):
    m.variables  # pylint: disable=pointless-statement
