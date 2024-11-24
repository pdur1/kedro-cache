from typing import List, Dict, Any
from kedro_cache.config.write_only_datasets_catalog import WRITE_ONLY_CLASSES

def get_hashable_dataset_names(dataset_names: List[str], catalog):
    hashable_datasets = []
    for name in dataset_names:
        dataset = catalog.datasets[name]
        if dataset.__class__ in WRITE_ONLY_CLASSES:
            continue
        hashable_datasets.append(name)
    return hashable_datasets