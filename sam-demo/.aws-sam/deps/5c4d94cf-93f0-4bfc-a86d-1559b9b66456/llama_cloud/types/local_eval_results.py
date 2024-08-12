# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .local_eval import LocalEval

try:
    import pydantic
    if pydantic.__version__.startswith("1."):
        raise ImportError
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LocalEvalResults(pydantic.BaseModel):
    """
    Schema for the result of a local evaluation.
    """

    project_id: str = pydantic.Field(description="The ID of the project.")
    eval_set_id: typing.Optional[str] = pydantic.Field(description="The ID of the local eval result set.")
    app_name: str = pydantic.Field(description="The name of the app.")
    eval_name: str = pydantic.Field(description="The name of the eval.")
    result: LocalEval = pydantic.Field(description="The eval results.")

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
