# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/naming_test.py
namer = naming.Namer({'temp': 1})
# temp is reserved in the global namespace
self.assertEqual('temp_1', namer.new_symbol('temp', set()))
# temp_2 is reserved in the local namespace
self.assertEqual('temp_3', namer.new_symbol('temp', set(('temp_2',))))
self.assertItemsEqual(('temp_1', 'temp_3'), namer.generated_names)
