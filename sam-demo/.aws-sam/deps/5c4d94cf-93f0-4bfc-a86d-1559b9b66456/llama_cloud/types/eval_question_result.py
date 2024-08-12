# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .eval_execution_params import EvalExecutionParams
from .metric_result import MetricResult
from .text_node import TextNode

try:
    import pydantic
    if pydantic.__version__.startswith("1."):
        raise ImportError
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EvalQuestionResult(pydantic.BaseModel):
    """
    Schema for the result of an eval question job.
    """

    eval_question_id: str = pydantic.Field(description="The ID of the question that was executed.")
    pipeline_id: str = pydantic.Field(description="The ID of the pipeline that the question was executed against.")
    source_nodes: typing.List[TextNode] = pydantic.Field(
        description="The nodes retrieved by the pipeline for the given question."
    )
    answer: str = pydantic.Field(description="The answer to the question.")
    eval_metrics: typing.Dict[str, MetricResult] = pydantic.Field(description="The eval metrics for the question.")
    eval_dataset_execution_id: str = pydantic.Field(
        description="The ID of the EvalDatasetJobRecord that this result was generated from."
    )
    eval_dataset_execution_params: EvalExecutionParams = pydantic.Field(
        description="The EvalExecutionParams that were used when this result was generated."
    )
    eval_finished_at: dt.datetime = pydantic.Field(description="The timestamp when the eval finished.")
    class_name: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
