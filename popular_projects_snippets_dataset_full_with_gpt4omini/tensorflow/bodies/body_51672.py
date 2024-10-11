# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/method_name_updater.py
"""Replaces the method_name in the specified signature_def.

    This will match and replace multiple sig defs iff tags is None (i.e when
    multiple `MetaGraph`s have a signature_def with the same key).
    If tags is not None, this will only replace a single signature_def in the
    `MetaGraph` with matching tags.

    Args:
      signature_key: Key of the signature_def to be updated.
      method_name: new method_name to replace the existing one.
      tags: A tag or sequence of tags identifying the `MetaGraph` to update. If
          None, all meta graphs will be updated.
    Raises:
      ValueError: if signature_key or method_name are not defined or
          if no metagraphs were found with the associated tags or
          if no meta graph has a signature_def that matches signature_key.
    """
if not signature_key:
    raise ValueError("`signature_key` must be defined.")
if not method_name:
    raise ValueError("`method_name` must be defined.")

if (tags is not None and not isinstance(tags, list)):
    tags = [tags]
found_match = False
for meta_graph_def in self._saved_model.meta_graphs:
    if tags is None or set(tags) == set(meta_graph_def.meta_info_def.tags):
        if signature_key not in meta_graph_def.signature_def:
            raise ValueError(
                f"MetaGraphDef associated with tags {tags} "
                f"does not have a signature_def with key: '{signature_key}'. "
                "This means either you specified the wrong signature key or "
                "forgot to put the signature_def with the corresponding key in "
                "your SavedModel.")
        meta_graph_def.signature_def[signature_key].method_name = method_name
        found_match = True

if not found_match:
    raise ValueError(
        f"MetaGraphDef associated with tags {tags} could not be found in "
        "SavedModel. This means either you specified invalid tags or your "
        "SavedModel does not have a MetaGraphDef with the specified tags.")
