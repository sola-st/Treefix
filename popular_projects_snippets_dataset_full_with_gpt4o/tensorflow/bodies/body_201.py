# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py
"""Get details about the full commit range tested by this invocation."""
head_info = git_pretty("HEAD", PRETTY_HEAD_INFO, n=1)
_, _, _, _, _, _, current_commit_date = head_info[0].split("\t")

query_earliest_included_commit = BQ_GET_EARLIEST_INCLUDED_COMMIT.format(
    table=TABLE_NAME,
    earlier_than_this_date=current_commit_date,
    artifact_id=FLAGS.artifact_id,
    team=FLAGS.team)

# --format=csv returns an empty string if no results, or else two lines:
# commit
# COMMIT_HASH
earliest_commit = bq(["query", "--format", "csv", "--nouse_legacy_sql"],
                     stdin=query_earliest_included_commit)

# Compute the commit/CL range since the last test
if earliest_commit:

    earliest_commit = earliest_commit.splitlines()[-1]  # Ignore CSV header
    early_author_date, early_cl, early_commit_date = git_pretty(
        earliest_commit, PRETTY_EARLY, n=1)[0].split("\t")

    all_range = "{commit}..HEAD".format(commit=earliest_commit)
    # Reversed: convert to chronological
    all_commits = ",".join(reversed(git_pretty(all_range, PRETTY_COMMIT)))
    all_changelists = ",".join(reversed(git_pretty(all_range, PRETTY_CL)))

    exit([
        earliest_commit, early_cl, early_author_date, early_commit_date,
        all_commits, all_changelists
    ])

# If the artifact has never been tracked before this commit
# Empty cells in CSV loads are loaded as NULL values
else:
    exit([""] * 6)
