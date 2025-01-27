# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
saveable_compat.force_checkpoint_conversion()

table_module = generate_checkpoint.TableModule()
table_module.lookup_table.insert(3, 9)
self.assertEqual(9, self.evaluate(table_module.lookup_table.lookup(3)))

ckpt = checkpoint.Checkpoint(table_module)
ckpt.read(_LEGACY_TABLE_CHECKPOINT_PATH).assert_consumed()
self.assertEqual(-1, self.evaluate(table_module.lookup_table.lookup(3)))
self.assertEqual(4, self.evaluate(table_module.lookup_table.lookup(2)))
