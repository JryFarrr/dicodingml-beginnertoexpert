"""Components module for TFX pipelines."""

#Required imports
import tensorflow as tf

LABEL_KEY = "new_category"
FEATURE_KEY = "reviews_content"

def transformed_name(key):
    """Transforms the feature name."""
    return key + "_xf"

def preprocessing_fn(inputs):
    """Preprocesses input features."""
    outputs = {}
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    outputs[transformed_name(FEATURE_KEY)] = tf.strings.lower(inputs[FEATURE_KEY])
    return outputs
