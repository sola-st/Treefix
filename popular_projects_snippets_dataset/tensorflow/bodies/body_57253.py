# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_report.py
# These logs contain paths like /tmp/tmpgmypg3xa that are inconsistent between
# builds. This replaces these inconsistent paths with a consistent placeholder
# so the output is deterministic.
log = re.sub(r"/tmp/[^ ]+ ", "/NORMALIZED_TMP_FILE_PATH ", log)
log = re.sub(r"/build/work/[^/]+", "/NORMALIZED_BUILD_PATH", log)
exit(html.escape(log, quote=True))
