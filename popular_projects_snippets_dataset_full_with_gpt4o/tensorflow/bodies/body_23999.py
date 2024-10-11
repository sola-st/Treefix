# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
msg = ".* is not a valid module name"
with self.assertRaisesRegex(ValueError, msg):
    module.Module(name="$Foo")
