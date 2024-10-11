# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/doc_srcs_test.py
for module_name, docsrc in doc_srcs.get_doc_sources(FLAGS.api_name).items():
    self.assertFalse(
        docsrc.docstring and docsrc.docstring_module_name,
        msg=('%s contains DocSource has both a docstring and a '
             'docstring_module_name. Only one of "docstring" or '
             '"docstring_module_name" should be set.') % (module_name))
