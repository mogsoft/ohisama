import numpy as np
import xarray

def find_integrations(ms):
    gap_index = []
    for index, value in enumerate(ms.time.data):

        if index == 0:
            previous = value
            continue

        delta = value - previous
        if delta > 0.05:
            gap_index.append(index)

        previous = value

    return gap_index

def get_block_indices(ms: xarray.Dataset) -> list[np.ndarray]:
    gaps = find_integrations(ms)

    indices = np.arange(ms.time.data.shape[0])
    block_indices = np.split(indices, gaps)

    return block_indices