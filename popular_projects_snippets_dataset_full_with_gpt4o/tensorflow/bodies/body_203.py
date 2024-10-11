# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py
"""Assemble one row of data about this artifact."""
(earliest_commit, early_cl, early_author_date, early_commit_date, all_commits,
 all_changelists) = get_all_tested_commits()

# Use UTC to make sure machines in different timezones load consistent data
current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
artifact_filename = ("NO_FILE" if not FLAGS.artifact else os.path.basename(
    FLAGS.artifact.name))
size_bytes = FLAGS.manual_bytes or os.path.getsize(FLAGS.artifact.name)
head_info = git_pretty("HEAD", PRETTY_HEAD_INFO, n=1)
all_head_info_items = head_info[0].split("\t")
exit([
    FLAGS.artifact_id,
    artifact_filename,
    *all_head_info_items,
    earliest_commit,
    early_cl,
    early_author_date,
    early_commit_date,
    all_commits,
    all_changelists,
    size_bytes,
    FLAGS.team,
    current_time,
    get_upload_path(),
    FLAGS.job,
    FLAGS.build_id,
])
