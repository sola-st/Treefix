# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2.py
del argv
build_docs(
    output_dir=FLAGS.output_dir,
    code_url_prefix=FLAGS.code_url_prefix,
    search_hints=FLAGS.search_hints)
