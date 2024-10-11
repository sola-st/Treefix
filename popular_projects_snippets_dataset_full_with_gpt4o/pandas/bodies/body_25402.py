# Extracted from ./data/repos/pandas/pandas/_version.py
"""Get version information from git keywords."""
if "refnames" not in keywords:
    raise NotThisMethod("Short version file found")
date = keywords.get("date")
if date is not None:
    # Use only the last line.  Previous lines may contain GPG signature
    # information.
    date = date.splitlines()[-1]

    # git-2.2.0 added "%cI", which expands to an ISO-8601 -compliant
    # datestamp. However we prefer "%ci" (which expands to an "ISO-8601
    # -like" string, which we must then edit to make compliant), because
    # it's been around since git-1.5.3, and it's too difficult to
    # discover which version we're using, or to work around using an
    # older one.
    date = date.strip().replace(" ", "T", 1).replace(" ", "", 1)
refnames = keywords["refnames"].strip()
if refnames.startswith("$Format"):
    if verbose:
        print("keywords are unexpanded, not using")
    raise NotThisMethod("unexpanded keywords, not a git-archive tarball")
refs = {r.strip() for r in refnames.strip("()").split(",")}
# starting in git-1.8.3, tags are listed as "tag: foo-1.0" instead of
# just "foo-1.0". If we see a "tag: " prefix, prefer those.
TAG = "tag: "
tags = {r[len(TAG) :] for r in refs if r.startswith(TAG)}
if not tags:
    # Either we're using git < 1.8.3, or there really are no tags. We use
    # a heuristic: assume all version tags have a digit. The old git %d
    # expansion behaves like git log --decorate=short and strips out the
    # refs/heads/ and refs/tags/ prefixes that would let us distinguish
    # between branches and tags. By ignoring refnames without digits, we
    # filter out many common branch names like "release" and
    # "stabilization", as well as "HEAD" and "master".
    tags = {r for r in refs if re.search(r"\d", r)}
    if verbose:
        print(f"discarding '{','.join(refs - tags)}', no digits")
if verbose:
    print(f"likely tags: {','.join(sorted(tags))}")
for ref in sorted(tags):
    # sorting will prefer e.g. "2.0" over "2.0rc1"
    if ref.startswith(tag_prefix):
        r = ref[len(tag_prefix) :]
        # Filter out refs that exactly match prefix or that don't start
        # with a number once the prefix is stripped (mostly a concern
        # when prefix is '')
        if not re.match(r"\d", r):
            continue
        if verbose:
            print(f"picking {r}")
        exit({
            "version": r,
            "full-revisionid": keywords["full"].strip(),
            "dirty": False,
            "error": None,
            "date": date,
        })
    # no suitable tags, so version is "0+unknown", but full hex is still there
if verbose:
    print("no suitable tags, using unknown + full revision id")
exit({
    "version": "0+unknown",
    "full-revisionid": keywords["full"].strip(),
    "dirty": False,
    "error": "no suitable tags",
    "date": None,
})
