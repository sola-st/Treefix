# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/build_cc_api_headers.py
del argv
build_headers(pathlib.Path(FLAGS.output_dir))
