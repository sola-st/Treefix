# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
if os.name == "nt":
    self.skipTest("os.symlink doesn't work uniformly on Windows.")

upgrade_dir = os.path.join(self.get_temp_dir(), "foo")
output_dir = os.path.join(self.get_temp_dir(), "bar")
os.mkdir(upgrade_dir)
file_a = os.path.join(upgrade_dir, "a.py")
file_b = os.path.join(upgrade_dir, "b.py")

with open(file_a, "a") as f:
    f.write("import foo as f")
os.symlink(file_a, file_b)

upgrader = ast_edits.ASTCodeUpgrader(RenameImports())
upgrader.process_tree(upgrade_dir, output_dir, copy_other_files=True)

new_file_a = os.path.join(output_dir, "a.py")
new_file_b = os.path.join(output_dir, "b.py")
self.assertTrue(os.path.islink(new_file_b))
self.assertEqual(new_file_a, os.readlink(new_file_b))
with open(new_file_a, "r") as f:
    self.assertEqual("import bar as f", f.read())
