"""
Pipeline Orchestrator
"""
from typing import Text
from tfx.orchestration import metadata, pipeline


def init_local_pipeline(tfx_components, pipeline_root_dir: Text, pipeline_name: str, metadata_dir: Text) -> pipeline.Pipeline:
    """Initializes a pipeline orchestrator with the given components, pipeline root, pipeline name, and metadata path.

    Args:
        tfx_components (list): The list of components to be included in the pipeline.
        pipeline_root_dir (Text): The root directory of the pipeline.
        pipeline_name (str): The name of the pipeline.
        metadata_dir (Text): The path to the metadata file.

    Returns:
        pipeline.Pipeline: The initialized pipeline object.
    """
    beam_args = [
        "--direct_running_mode=multi_processing",
        "--direct_num_workers=0",
    ]

    return pipeline.Pipeline(
        pipeline_name=pipeline_name,
        pipeline_root=pipeline_root_dir,
        components=tfx_components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(metadata_dir),
        beam_pipeline_args=beam_args,
    )
