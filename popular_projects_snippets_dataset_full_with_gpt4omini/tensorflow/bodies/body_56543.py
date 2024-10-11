# Extracted from ./data/repos/tensorflow/tensorflow/lite/g3doc/tools/build_java_api_docs.py
root = pathlib.Path(__file__).resolve()
all_deps = [SOURCE_PATH_CORE, SOURCE_PATH_SUPPORT, SOURCE_PATH_ODML]
# Keep searching upwards for a root that hosts the various dependencies. We
# test `root.name` to ensure we haven't hit /.
while root.name and not (exists := exists_maybe_nested(all_deps, root)):
    root = root.parent
if not exists:
    raise FileNotFoundError('Could not find dependencies.')

with tempfile.TemporaryDirectory() as merge_tmp_dir:
    # Merge the combined API sources into a single location.
    merged_temp_dir = pathlib.Path(merge_tmp_dir)
    overlay(resolve_nested_dir(SOURCE_PATH_CORE, root), merged_temp_dir)
    overlay(resolve_nested_dir(SOURCE_PATH_GPU, root), merged_temp_dir)
    overlay(resolve_nested_dir(SOURCE_PATH_SUPPORT, root), merged_temp_dir)
    overlay(resolve_nested_dir(SOURCE_PATH_METADATA, root), merged_temp_dir)
    overlay(resolve_nested_dir(SOURCE_PATH_ODML, root), merged_temp_dir)

    if gms_path := os.getenv('GMS_PATH'):
        # Play Services code needs to be massaged into a Java directory structure.
        overlay(gms_path, merged_temp_dir / 'org/tensorflow/lite/task/gms')

    gen_java.gen_java_docs(
        package=['org.tensorflow.lite', 'com.google.android.odml'],
        source_path=merged_temp_dir,
        output_dir=pathlib.Path(_OUT_DIR.value),
        site_path=pathlib.Path(_SITE_PATH.value),
        section_labels=SECTION_LABELS,
        federated_docs={k: root / v for k, v in EXTERNAL_APIS.items()})
