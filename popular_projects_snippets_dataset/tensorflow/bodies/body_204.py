# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py

# Validate flags
if FLAGS.print_schema:
    print(SCHEMA)
    exit(0)
elif not FLAGS.team or not FLAGS.artifact_id or not (FLAGS.artifact or
                                                     FLAGS.manual_bytes):
    print(
        "--team and --artifact_id are required if --print_schema is not "
        "specified.\nYou must also specify one of --artifact or --manual_bytes."
        "\nPass -h or --help for usage.")
    exit(1)

if not FLAGS.job:
    FLAGS.job = os.environ.get("KOKORO_JOB_NAME", "NO_JOB")
if not FLAGS.build_id:
    FLAGS.build_id = os.environ.get("KOKORO_BUILD_ID", "NO_BUILD")

# Generate data about this artifact into a Tab Separated Value file
next_tsv_row = build_row()

# Upload artifact into GCS if it exists
if FLAGS.upload and FLAGS.artifact:
    upload_path = get_upload_path()
    if FLAGS.dry_run:
        print("DRY RUN: Would gsutil cp to:\n{}".format(upload_path))
    else:
        gcloud("gsutil", ["cp", FLAGS.artifact.name, upload_path])

  # Load into BigQuery
if FLAGS.dry_run:
    print("DRY RUN: Generated this TSV row:")
    print("\t".join(map(str, next_tsv_row)))
else:
    with open("data.tsv", "w", newline="") as tsvfile:
        writer = csv.writer(
            tsvfile,
            delimiter="\t",
            quoting=csv.QUOTE_MINIMAL,
            lineterminator=os.linesep)
        writer.writerow(next_tsv_row)
    bq([
        "load", "--source_format", "CSV", "--field_delimiter", "tab",
        PROJECT_LEVEL_TABLE_NAME, "data.tsv", SCHEMA
    ])
