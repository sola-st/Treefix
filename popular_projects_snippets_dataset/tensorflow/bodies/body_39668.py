# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
saveable_compat.force_checkpoint_conversion()

table_module = generate_checkpoint.TableModule()
table_module.lookup_table.insert(3, 9)
ckpt = checkpoint.Checkpoint(table_module)
checkpoint_directory = self.get_temp_dir()
checkpoint_path = os.path.join(checkpoint_directory, "ckpt")
ckpt.write(checkpoint_path)

new_table_module = generate_checkpoint.TableModule()
self.assertEqual(-1, self.evaluate(new_table_module.lookup_table.lookup(3)))

new_ckpt = checkpoint.Checkpoint(new_table_module)
new_ckpt.read(checkpoint_path).assert_consumed()
self.assertEqual(9, self.evaluate(new_table_module.lookup_table.lookup(3)))
