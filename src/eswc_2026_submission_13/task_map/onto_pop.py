#!/usr/bin/env python

import eswc_2026_submission_13.metrics.datasets.onto_pop as dataset_metrics
import eswc_2026_submission_13.metrics.results.onto_pop as pred_metrics
import polars as pl
from eswc_2026_submission_13.model.common import format_response

task_types = {
    "binary_classify": {
        "dataset_metrics": dataset_metrics.TermTypingBinaryClassification,
        "pred_metrics": pred_metrics.binary_classify,
        "format_response": {
            "function": format_response.binary_classify,
            "return_dtype": pl.Boolean,
            "df_columns": ["Individual", "Class"],
        },
    },
    "ranked_retrieval": {
        "dataset_metrics": dataset_metrics.TermTypingRankedRetrieval,
        "pred_metrics": pred_metrics.ranked_retrieval,
        "format_response": {
            "function": format_response.ranked_retrieval,
            "return_dtype": pl.List(pl.String),
            "df_columns": ["Individual"],
        },
    },
}
