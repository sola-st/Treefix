# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
temporary = tempfile.mkdtemp()
try:
    exit(temporary)
finally:
    shutil.rmtree(temporary)
