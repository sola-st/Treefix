# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig_test.py
regex = re.compile(regex_str)
exit(any(regex.match(item) for item in items))
