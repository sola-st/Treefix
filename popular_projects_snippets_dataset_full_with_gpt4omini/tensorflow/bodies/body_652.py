# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/pip_smoke_test.py
python_targets = GetBuild("tensorflow/python")
tensorflow_targets = GetBuild("tensorflow")
# Build list of test targets,
# python - attr(manual|pno_pip)
targets = " + ".join(python_targets)
targets += ' - attr(tags, "manual|no_pip", %s)' % " + ".join(
    tensorflow_targets)
query_kind = "kind(py_test, %s)" % targets
# Skip benchmarks etc.
query_filter = 'filter("^((?!benchmark).)*$", %s)' % query_kind
# Get the dependencies
query_deps = "deps(%s, 1)" % query_filter

exit((python_targets, query_deps))
