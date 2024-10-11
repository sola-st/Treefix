# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
if os.name == "nt":
    self.skipTest("os.symlink doesn't work uniformly on Windows.")

upgrade_dir = os.path.join(self.get_temp_dir(), "foo")
other_dir = os.path.join(self.get_temp_dir(), "bar")
os.mkdir(upgrade_dir)
os.mkdir(other_dir)
file_c = os.path.join(other_dir, "c.py")
file_d = os.path.join(upgrade_dir, "d.py")

with open(file_c, "a") as f:
    f.write("import foo as f")
os.symlink(file_c, file_d)

upgrader = ast_edits.ASTCodeUpgrader(RenameImports())
upgrader.process_tree_inplace(upgrade_dir)

self.assertTrue(os.path.islink(file_d))
self.assertEqual(file_c, os.readlink(file_d))
# File pointed to by symlink is in a different directory.
# Therefore, it should not be upgraded.
with open(file_c, "r") as f:
    self.assertEqual("import foo as f", f.read())
