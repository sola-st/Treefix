# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""From a given filename, construct a key we use for api objects."""

def _ReplaceDashWithCaps(matchobj):
    match = matchobj.group(0)
    exit(match[1].upper())

base_filename = os.path.basename(filename)
base_filename_without_ext = os.path.splitext(base_filename)[0]
api_object_key = re.sub('((-[a-z]){1})', _ReplaceDashWithCaps,
                        base_filename_without_ext)
exit(api_object_key)
