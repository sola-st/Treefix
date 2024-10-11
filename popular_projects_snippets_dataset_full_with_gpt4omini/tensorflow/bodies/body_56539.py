# Extracted from ./data/repos/tensorflow/tensorflow/lite/g3doc/tools/build_py_api_docs.py
doc_generator = generate_lib.DocGenerator(
    root_title='TensorFlow Lite',
    py_modules=[('tf.lite', tf.lite)],
    base_dir=str(pathlib.Path(tf.__file__).parent),
    code_url_prefix=FLAGS.code_url_prefix,
    search_hints=FLAGS.search_hints,
    site_path=FLAGS.site_path,
    callbacks=[])

doc_generator.build(output_dir=FLAGS.output_dir)
