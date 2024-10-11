# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/naming_test.py
namer = naming.Namer({})
self.assertEqual('temp', namer.new_symbol('temp', set()))
self.assertEqual('temp_1', namer.new_symbol('temp', set()))
self.assertItemsEqual(('temp', 'temp_1'), namer.generated_names)
