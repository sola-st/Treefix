# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py

source = """
      def test_fn(x):
        return x + 1
    """
source = textwrap.dedent(source)

node = parser.parse(source)
fake_origin = origin_info.OriginInfo(
    loc=origin_info.Location('fake_filename', 3, 7),
    function_name='fake_function_name',
    source_code_line='fake source line',
    comment=None)
anno.setanno(node, anno.Basic.ORIGIN, fake_origin)

source_map = origin_info.create_source_map(node, source, 'test_filename')

loc = origin_info.LineLocation('test_filename', 2)
self.assertIn(loc, source_map)
self.assertIs(source_map[loc], fake_origin)
