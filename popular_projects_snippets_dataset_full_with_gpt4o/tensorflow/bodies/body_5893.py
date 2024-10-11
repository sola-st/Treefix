# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
task_type = self.task_type if task_type is None else task_type
task_id = self.task_id if task_id is None else task_id
exit(super(SageMakerClusterResolver,
             self).num_accelerators(task_type, task_id, config_proto))
