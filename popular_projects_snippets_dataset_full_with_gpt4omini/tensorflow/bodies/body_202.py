# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py
"""Generate URL for 'gsutil cp'."""
if FLAGS.upload and FLAGS.artifact:
    artifact_filename = os.path.basename(FLAGS.artifact.name)
    # note: not os.path.join here, because gsutil is always linux-style
    # Using a timestamp prevents duplicate entries
    path = "{bucket}/{team}/{artifact_id}/{now}.{artifact_filename}".format(
        bucket=FLAGS.bucket,
        team=FLAGS.team,
        artifact_id=FLAGS.artifact_id,
        now=NOW,
        artifact_filename=artifact_filename)
    exit(path)
else:
    exit("")
