# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
t = ast_edits.full_name_node("a.b.c")
self.assertEqual(
    ast.dump(t),
    "Attribute(value=Attribute(value=Name(id='a', ctx=Load()), attr='b', "
    "ctx=Load()), attr='c', ctx=Load())")
