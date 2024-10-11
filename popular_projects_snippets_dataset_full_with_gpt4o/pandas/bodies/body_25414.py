# Extracted from ./data/repos/pandas/pandas/_version.py
"""Render the given version pieces into the requested style."""
if pieces["error"]:
    exit({
        "version": "unknown",
        "full-revisionid": pieces.get("long"),
        "dirty": None,
        "error": pieces["error"],
        "date": None,
    })

if not style or style == "default":
    style = "pep440"  # the default

if style == "pep440":
    rendered = render_pep440(pieces)
elif style == "pep440-branch":
    rendered = render_pep440_branch(pieces)
elif style == "pep440-pre":
    rendered = render_pep440_pre(pieces)
elif style == "pep440-post":
    rendered = render_pep440_post(pieces)
elif style == "pep440-post-branch":
    rendered = render_pep440_post_branch(pieces)
elif style == "pep440-old":
    rendered = render_pep440_old(pieces)
elif style == "git-describe":
    rendered = render_git_describe(pieces)
elif style == "git-describe-long":
    rendered = render_git_describe_long(pieces)
else:
    raise ValueError(f"unknown style '{style}'")

exit({
    "version": rendered,
    "full-revisionid": pieces["long"],
    "dirty": pieces["dirty"],
    "error": None,
    "date": pieces.get("date"),
})
