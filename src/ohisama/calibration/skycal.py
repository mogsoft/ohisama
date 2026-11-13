from typing import Any

import xarray

import numpy as np

from ohisama.utilities import tools

def solve(chunk: xarray.Dataset) -> dict[str, list[Any]]:
    block_indices = tools.get_block_indices(chunk)

    solutions = []
    time_centroids = []
    effective_integrations = []

    for integration in block_indices:
        block = chunk.isel(time=integration[:-1])
        solution, time_centroid, effective_integration = _weighted_time_average(block=block)
        solutions.append(solution)
        time_centroids.append(time_centroid)
        effective_integrations.append(effective_integration)

    return {
        "solution": solutions,
        "time_centroid": time_centroids,
        "effective_integration": effective_integrations,
    }

def _weighted_time_average(block: xarray.Dataset) -> tuple[Any, Any, Any]:
    n_time, n_baseline, n_frequency, n_polarization = block.VISIBILITY.data.shape

    time_centroid = block.time.mean(axis=0).compute()
    effective_integration = block.EFFECTIVE_INTEGRATION_TIME.data.sum(axis=0).compute()

    valid_data = np.logical_not(block.FLAG.data) * block.VISIBILITY.data
    weight = np.tile(block.EFFECTIVE_INTEGRATION_TIME.data[..., np.newaxis, np.newaxis], [1, 1, n_frequency, n_polarization])

    weighted_sum = (valid_data * weight).sum(axis=0)
    weight_total = (np.logical_not(block.FLAG.data) * weight).sum(axis=0)


    return (weighted_sum / weight_total).compute(), time_centroid, effective_integration