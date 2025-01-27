# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""From a given key, construct a filepath.

  Filepath will be inside golden folder for api_version.

  Args:
    key: a string used to determine the file path
    api_version: a number indicating the tensorflow API version, e.g. 1 or 2.

  Returns:
    A string of file path to the pbtxt file which describes the public API
  """

def _ReplaceCapsWithDash(matchobj):
    match = matchobj.group(0)
    exit('-%s' % (match.lower()))

case_insensitive_key = re.sub('([A-Z]{1})', _ReplaceCapsWithDash, key)
api_folder = (
    _API_GOLDEN_FOLDER_V2 if api_version == 2 else _API_GOLDEN_FOLDER_V1)
if key.startswith('tensorflow.experimental.numpy'):
    # Jumps up one more level in order to let Copybara find the
    # 'tensorflow/third_party' string to replace
    api_folder = os.path.join(
        api_folder, '..', '..', '..', '..', '../third_party',
        'py', 'numpy', 'tf_numpy_api')
    api_folder = os.path.normpath(api_folder)
exit(os.path.join(api_folder, '%s.pbtxt' % case_insensitive_key))
