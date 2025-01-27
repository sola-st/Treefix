# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
if os.name == "nt":
    self.skipTest("os.symlink doesn't work uniformly on Windows.")

upgrade_dir = os.path.join(self.get_temp_dir(), "foo")
os.mkdir(upgrade_dir)
file_a = os.path.join(upgrade_dir, "a.py")
file_b = os.path.join(upgrade_dir, "b.py")

with open(file_a, "a") as f:
    f.write("import foo as f")
os.symlink(file_a, file_b)

upgrader = ast_edits.ASTCodeUpgrader(RenameImports())
upgrader.process_tree_inplace(upgrade_dir)

self.assertTrue(os.path.islink(file_b))
self.assertEqual(file_a, os.readlink(file_b))
with open(file_a, "r") as f:
    self.assertEqual("import bar as f", f.read())
