# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2_test.py
generate2.MIN_NUM_FILES_EXPECTED = 1
output_dir = pathlib.Path(googletest.GetTempDir())/'output'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)
generate2.build_docs(
    output_dir=output_dir,
    code_url_prefix='',
    search_hints=True,
)

raw_ops_page = (output_dir/'tf/raw_ops.md').read_text()
self.assertIn('/tf/raw_ops/Add.md', raw_ops_page)

toc = yaml.safe_load((output_dir / 'tf/_toc.yaml').read_text())
self.assertEqual({
    'title': 'Overview',
    'path': '/tf_overview'
}, toc['toc'][0]['section'][0])
redirects = yaml.safe_load((output_dir / 'tf/_redirects.yaml').read_text())
self.assertIn({'from': '/tf_overview', 'to': '/tf'}, redirects['redirects'])
