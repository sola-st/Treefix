# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
node, source = parser.parse_entity(test_fn, ())
origin_info.resolve_entity(node, source, test_fn)
# Creating a source map with the source code as output will create
# an identity map.
exit(origin_info.create_source_map(node, source, 'test_filename'))
