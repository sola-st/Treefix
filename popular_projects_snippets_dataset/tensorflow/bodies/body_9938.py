# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/doc_srcs_test.py
for _, docsrc in doc_srcs.get_doc_sources(FLAGS.api_name).items():
    if docsrc.docstring_module_name:
        doc_module_name = '.'.join([
            FLAGS.package, docsrc.docstring_module_name])
        self.assertIn(
            doc_module_name, sys.modules,
            msg=('docsources_module %s is not a valid module under %s.' %
                 (docsrc.docstring_module_name, FLAGS.package)))
