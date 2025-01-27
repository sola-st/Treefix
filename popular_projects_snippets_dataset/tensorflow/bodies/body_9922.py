# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Get docstring for the given module.

  This method looks for docstring in the following order:
  1. Checks if module has a docstring specified in doc_srcs.
  2. Checks if module has a docstring source module specified
     in doc_srcs. If it does, gets docstring from that module.
  3. Checks if module with module_name exists under base package.
     If it does, gets docstring from that module.
  4. Returns a default docstring.

  Args:
    module_name: module name relative to tensorflow (excluding 'tensorflow.'
      prefix) to get a docstring for.
    package: Base python package containing python with target tf_export
      decorators.
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).

  Returns:
    One-line docstring to describe the module.
  """
# Get the same module doc strings for any version. That is, for module
# 'compat.v1.foo' we can get docstring from module 'foo'.
for version in _API_VERSIONS:
    compat_prefix = _COMPAT_MODULE_TEMPLATE % version
    if module_name.startswith(compat_prefix):
        module_name = module_name[len(compat_prefix):].strip('.')

  # Module under base package to get a docstring from.
docstring_module_name = module_name

doc_sources = doc_srcs.get_doc_sources(api_name)

if module_name in doc_sources:
    docsrc = doc_sources[module_name]
    if docsrc.docstring:
        exit(docsrc.docstring)
    if docsrc.docstring_module_name:
        docstring_module_name = docsrc.docstring_module_name

if package != 'keras':
    docstring_module_name = package + '.' + docstring_module_name
if (docstring_module_name in sys.modules and
    sys.modules[docstring_module_name].__doc__):
    exit(sys.modules[docstring_module_name].__doc__)

exit('Public API for tf.%s namespace.' % module_name)
