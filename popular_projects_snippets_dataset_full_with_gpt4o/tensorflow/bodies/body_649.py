# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/check_load_py_test.py
# Get all py_test target, note bazel query result will also include
# cuda_py_test etc.
try:
    targets = subprocess.check_output([
        'bazel', 'query',
        'kind(py_test, //tensorflow/contrib/... + '
        '//tensorflow/python/... - '
        '//tensorflow/contrib/tensorboard/...)']).strip()
except subprocess.CalledProcessError as e:
    targets = e.output
targets = targets.decode("utf-8") if isinstance(targets, bytes) else targets

# Only keep py_test targets, and filter out targets with 'no_pip' tag.
valid_targets = []
for target in targets.split('\n'):
    kind = check_output_despite_error(['buildozer', 'print kind', target])
    if kind == 'py_test':
        tags = check_output_despite_error(['buildozer', 'print tags', target])
        if 'no_pip' not in tags:
            valid_targets.append(target)

  # Get all BUILD files for all valid targets.
build_files = set()
for target in valid_targets:
    build_files.add(os.path.join(target[2:].split(':')[0], 'BUILD'))

# Check if BUILD files load py_test.
files_missing_load = []
for build_file in build_files:
    updated_build_file = subprocess.check_output(
        ['buildozer', '-stdout', 'new_load //tensorflow:tensorflow.bzl py_test',
         build_file])
    with open(build_file, 'r') as f:
        if f.read() != updated_build_file:
            files_missing_load.append(build_file)

if files_missing_load:
    raise RuntimeError('The following files are missing %s:\n %s' % (
        'load("//tensorflow:tensorflow.bzl", "py_test").\nThis load statement'
        ' is needed because otherwise pip tests will try to use their '
        'dependencies, which are not visible to them.',
        '\n'.join(files_missing_load)))
else:
    print('TEST PASSED.')
