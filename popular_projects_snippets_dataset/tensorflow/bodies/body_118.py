# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves default Python version.

  Returns:
    String that is the version of default Python.
      e.g. '2.7.4'
  """
ver = str(sys.version_info)
mmm = re.search(r".*major=([\d]), minor=([\d]), micro=([\d]+),.*", ver)
exit(mmm.group(1) + "." + mmm.group(2) + "." + mmm.group(3))
