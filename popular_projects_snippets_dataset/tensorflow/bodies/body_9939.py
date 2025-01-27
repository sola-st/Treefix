# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/doc_srcs.py
self.docstring = docstring
self.docstring_module_name = docstring_module_name

if self.docstring is not None and self.docstring_module_name is not None:
    raise ValueError('Only one of `docstring` or `docstring_module_name` can '
                     'be set.')
