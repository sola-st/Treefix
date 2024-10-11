# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
# This comment will be missed because the tokenizer fails to reach it.
source = '   lambda: foo([], bar=1)), baz=2)()'
clean_source = 'lambda: foo([], bar=1)'
node = parser.parse(clean_source).value
origin_info.resolve(node, source, 'test_file', 10, 10)

def_origin = anno.getanno(node, anno.Basic.ORIGIN)
self.assertEqual(def_origin.loc.lineno, 10)
self.assertEqual(def_origin.loc.col_offset, 10)
self.assertEqual(def_origin.source_code_line, source)
self.assertIsNone(def_origin.comment)
