"""
Make Components
"""
from tfx import v1 as tfx

def init_components(data_path, module_file, serving_model_dir):
    """Creates a TFX pipeline for user sentiment analysis.

    Args:
        pipeline_name (str): The name of the pipeline.
        pipeline_root (str): The root directory of the pipeline.
        data_path (str): The path to the data.
        module_file (str): The file containing module code.
        serving_model_dir (str): The directory to store the serving model.

    Returns:
        list: A list of TFX components.
    """
    components = []

    # ExampleGen component
    example_gen = tfx.components.CsvExampleGen(input_base=data_path)
    components.append(example_gen)

    # StatisticsGen component
    statistics_gen = tfx.components.StatisticsGen(examples=example_gen.outputs['examples'])
    components.append(statistics_gen)

    # SchemaGen component
    schema_gen = tfx.components.SchemaGen(statistics=statistics_gen.outputs['statistics'])
    components.append(schema_gen)

    # Trainer component
    train_args = tfx.proto.TrainArgs(num_steps=1000)
    eval_args = tfx.proto.EvalArgs(num_steps=500)
    trainer = tfx.components.Trainer(
        module_file=module_file,
        examples=example_gen.outputs['examples'],
        schema=schema_gen.outputs['schema'],
        train_args=train_args,
        eval_args=eval_args
    )
    components.append(trainer)

    # Pusher component
    push_destination = tfx.proto.PushDestination(
        filesystem=tfx.proto.PushDestination.Filesystem(
            base_directory=serving_model_dir
        )
    )
    pusher = tfx.components.Pusher(
        model=trainer.outputs['model'],
        push_destination=push_destination
    )
    components.append(pusher)

    return components
