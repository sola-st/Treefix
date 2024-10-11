# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/doc_srcs_test.py
for module_name in doc_srcs.get_doc_sources(FLAGS.api_name):
    # Convert module_name to corresponding __init__.py file path.
    file_path = module_name.replace('.', '/')
    if file_path:
        file_path += '/'
    file_path += '__init__.py'

    self.assertIn(
        file_path, FLAGS.outputs,
        msg='%s is not a valid API module' % module_name)
