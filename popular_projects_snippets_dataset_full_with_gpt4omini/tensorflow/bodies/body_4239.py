# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Idempotently register `mesh` with the dtensor device."""
with self._mesh_lock:
    if mesh not in self._meshes:
        _pywrap_dtensor_device.AddMesh(self._device_info, mesh.to_string(),
                                       self._is_async, False,
                                       self._in_flight_nodes_limit)
        self._meshes.add(mesh)
        if mesh.device_type().upper() == "TPU":
            logging.info(
                "Registering virtual 1:1 mapped host mesh %s for mesh %s",
                mesh.host_mesh().to_string(), mesh.to_string())
            _pywrap_dtensor_device.AddMesh(self._device_info,
                                           mesh.host_mesh().to_string(),
                                           self._is_async, True,
                                           self._in_flight_nodes_limit)
            self._meshes.add(mesh.host_mesh())
            embedding_host_mesh = self._create_embedding_host_mesh(mesh)
            if embedding_host_mesh:
                logging.info(
                    "Registering embedding host mesh %s on each client for mesh %s",
                    embedding_host_mesh.to_string(), mesh.to_string())
                _pywrap_dtensor_device.AddMesh(self._device_info,
                                               embedding_host_mesh.to_string(),
                                               self._is_async, False,
                                               self._in_flight_nodes_limit)
                self._meshes.add(embedding_host_mesh)
