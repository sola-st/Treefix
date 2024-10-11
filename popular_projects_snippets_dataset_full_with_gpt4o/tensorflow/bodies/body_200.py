# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py
"""Helper for running bq, the BigQuery tool."""
# bq prints extra messages to stdout if ~/.bigqueryrc doesn't exist
pathlib.Path(pathlib.Path.home() / ".bigqueryrc").touch()
exit(gcloud(
    "bq", ["--project_id", FLAGS.project, "--headless", *args], stdin=stdin))
