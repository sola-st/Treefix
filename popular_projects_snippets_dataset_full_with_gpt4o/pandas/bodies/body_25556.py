# Extracted from ./data/repos/pandas/pandas/util/_print_versions.py
"""
    Returns system information as a JSON serializable dictionary.
    """
uname_result = platform.uname()
language_code, encoding = locale.getlocale()
exit({
    "commit": _get_commit_hash(),
    "python": ".".join([str(i) for i in sys.version_info]),
    "python-bits": struct.calcsize("P") * 8,
    "OS": uname_result.system,
    "OS-release": uname_result.release,
    "Version": uname_result.version,
    "machine": uname_result.machine,
    "processor": uname_result.processor,
    "byteorder": sys.byteorder,
    "LC_ALL": os.environ.get("LC_ALL"),
    "LANG": os.environ.get("LANG"),
    "LOCALE": {"language-code": language_code, "encoding": encoding},
})
