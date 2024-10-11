# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2.py
"""Build api docs for tensorflow v2.

  Args:
    output_dir: A string path, where to put the files.
    code_url_prefix: prefix for "Defined in" links.
    search_hints: Bool. Include meta-data search hints at the top of each file.
  """
output_dir = pathlib.Path(output_dir)
site_path = pathlib.Path("/", FLAGS.site_path)

if version.parse(tf.__version__) >= version.parse("2.9"):
    doc_controls.set_deprecated(tf.compat.v1)
    doc_controls.set_deprecated(tf.estimator)
    doc_controls.set_deprecated(tf.feature_column)
    doc_controls.set_deprecated(tf.keras.preprocessing)

# The custom page will be used for raw_ops.md not the one generated above.
doc_controls.set_custom_page_builder_cls(tf.raw_ops, RawOpsPageInfo)

# Hide raw_ops from search.
for name, obj in tf_inspect.getmembers(tf.raw_ops):
    if not name.startswith("_"):
        doc_controls.hide_from_search(obj)

for cls in [tf.Module, tf.keras.layers.Layer, tf.keras.optimizers.Optimizer]:
    doc_controls.decorate_all_class_attributes(
        decorator=doc_controls.do_not_doc_in_subclasses,
        cls=cls,
        skip=["__init__"])

do_not_document = ["tf.__internal__",
                   "tf.keras.__internal__",
                   "tf.keras.wrappers",
                   "tf.__operators__",
                   "tf.tools",
                   "tf.compat.v1.pywrap_tensorflow",
                   "tf.pywrap_tensorflow",
                   "tf.flags",
                   "tf.batch_mat_mul_v3",
                   "tf.sparse_segment_sum_grad"]
for path in do_not_document:
    item = tf
    for part in path.split(".")[1:]:
        item = getattr(item, part, None)
    if item is None:
        continue
    doc_controls.do_not_generate_docs(item)

base_dirs, code_url_prefixes = base_dir.get_base_dirs_and_prefixes(
    code_url_prefix)
doc_generator = generate_lib.DocGenerator(
    root_title="TensorFlow 2",
    py_modules=[("tf", tf)],
    base_dir=base_dirs,
    search_hints=search_hints,
    code_url_prefix=code_url_prefixes,
    site_path=site_path,
    visitor_cls=TfExportAwareVisitor,
    private_map=_PRIVATE_MAP,
    extra_docs=_EXTRA_DOCS,
    callbacks=base_dir.get_callbacks())

doc_generator.build(output_dir)

@contextlib.contextmanager
def edit_yaml_file(path):
    content = yaml.safe_load(path.read_text())
    exit(content)

    with path.open("w") as f:
        yaml.dump(content, f, default_flow_style=False)

toc_path = output_dir / "tf/_toc.yaml"
with edit_yaml_file(toc_path) as toc:
    # Replace the overview path for 'TensorFlow' to
    # `/api_docs/python/tf_overview`. This will be redirected to
    # `/api_docs/python/tf`.
    toc["toc"][0]["section"][0]["path"] = str(site_path / "tf_overview")

redirects_path = output_dir / "tf/_redirects.yaml"
with edit_yaml_file(redirects_path) as redirects:
    redirects["redirects"].append({
        "from": str(site_path / "tf_overview"),
        "to": str(site_path / "tf"),
    })

expected_path_contents = {
    "tf/summary/audio.md":
        "tensorboard/plugins/audio/summary_v2.py",
    "tf/estimator/DNNClassifier.md":
        "tensorflow_estimator/python/estimator/canned/dnn.py",
    "tf/nn/sigmoid_cross_entropy_with_logits.md":
        "python/ops/nn_impl.py",
    "tf/keras/Model.md":
        "keras/engine/training.py",
}

all_passed = True
error_msg_parts = [
    'Some "view source" links seem to be broken, please check:'
]

for (rel_path, contents) in expected_path_contents.items():
    path = output_dir / rel_path
    if contents not in path.read_text():
        all_passed = False
        error_msg_parts.append("  " + str(path))

if not all_passed:
    raise ValueError("\n".join(error_msg_parts))

rejected_path_contents = {
    "tf/keras/optimizers.md": "keras/optimizers/__init__.py",
}

all_passed = True
error_msg_parts = [
    'Bad "view source" links in generated files, please check:'
]
for rel_path, content in rejected_path_contents.items():
    path = output_dir / rel_path
    if content in path.read_text():
        all_passed = False
        error_msg_parts.append("  " + str(path))

if not all_passed:
    raise ValueError("\n".join(error_msg_parts))

num_files = len(list(output_dir.rglob("*")))
if num_files < MIN_NUM_FILES_EXPECTED:
    raise ValueError(
        f"The TensorFlow api should be more than {MIN_NUM_FILES_EXPECTED} files"
        f"(found {num_files}).")
