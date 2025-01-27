# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns a union of all the ClusterSpecs from the ClusterResolvers.

    Returns:
      A ClusterSpec containing host information merged from all the underlying
      ClusterResolvers.

    Raises:
      KeyError: If there are conflicting keys detected when merging two or
      more dictionaries, this exception is raised.

    Note: If there are multiple ClusterResolvers exposing ClusterSpecs with the
    same job name, we will merge the list/dict of workers.

    If *all* underlying ClusterSpecs expose the set of workers as lists, we will
    concatenate the lists of workers, starting with the list of workers from
    the first ClusterResolver passed into the constructor.

    If *any* of the ClusterSpecs expose the set of workers as a dict, we will
    treat all the sets of workers as dicts (even if they are returned as lists)
    and will only merge them into a dict if there is no conflicting keys. If
    there is a conflicting key, we will raise a `KeyError`.
    """

merged_cluster = {}

# We figure out whether it is all lists for a particular job, or whether
# there are dicts inside.
for cluster_resolver in self._cluster_resolvers:
    cluster_spec = cluster_resolver.cluster_spec()
    cluster_dict = cluster_spec.as_dict()

    for job_name, tasks in cluster_dict.items():
        if job_name in merged_cluster:
            # If we see a dict, then we write a dict out regardless.
            if isinstance(tasks, dict):
                merged_cluster[job_name] = {}
        else:
            # We take whichever type is present.
            if isinstance(tasks, list):
                merged_cluster[job_name] = []
            else:
                merged_cluster[job_name] = {}

    # We then do the merge as appropriate in merged_cluster[job].
for cluster_resolver in self._cluster_resolvers:
    cluster_spec = cluster_resolver.cluster_spec()
    cluster_dict = cluster_spec.as_dict()

    for job_name, tasks in cluster_dict.items():
        if isinstance(merged_cluster[job_name], list):
            # We all have lists, we can just concatenate and be done.
            merged_cluster[job_name].extend(tasks)
        else:
            if isinstance(tasks, list):
                # We convert to a dictionary if the type is a list.
                task_dict = dict(zip(range(0, len(tasks)), tasks))
            else:
                # We can simply make a copy (for update) and be done.
                task_dict = tasks.copy()

            # We detect if there are duplicates, and raise an error if so.
            task_keys = set(task_dict)
            merged_keys = set(merged_cluster[job_name].keys())
            intersected_keys = task_keys.intersection(merged_keys)
            if intersected_keys:
                raise KeyError('Duplicate keys detected when merging two '
                               'ClusterSpecs: %s' % repr(intersected_keys))

            # We do the merge after all the processing.
            merged_cluster[job_name].update(task_dict)

exit(ClusterSpec(merged_cluster))
