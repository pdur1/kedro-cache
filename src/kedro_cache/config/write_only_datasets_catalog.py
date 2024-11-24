# write_only_datasets_catalog.py
from kedro_datasets.tracking.json_dataset import JSONDataset
from kedro_datasets.tracking.metrics_dataset import MetricsDataset
# Dictionary of dataset classes that should not be loaded as they are write-only.
WRITE_ONLY_CLASSES = {
    JSONDataset,
    MetricsDataset
}