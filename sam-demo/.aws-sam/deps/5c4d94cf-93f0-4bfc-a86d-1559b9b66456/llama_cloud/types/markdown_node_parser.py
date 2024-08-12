# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic
    if pydantic.__version__.startswith("1."):
        raise ImportError
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MarkdownNodeParser(pydantic.BaseModel):
    """
    Markdown node parser.

    Splits a document into Nodes using custom Markdown splitting logic.

    Args:
    include_metadata (bool): whether to include metadata in nodes
    include_prev_next_rel (bool): whether to include prev/next relationships
    """

    include_metadata: typing.Optional[bool] = pydantic.Field(
        description="Whether or not to consider metadata when splitting."
    )
    include_prev_next_rel: typing.Optional[bool] = pydantic.Field(description="Include prev/next node relationships.")
    callback_manager: typing.Optional[typing.Dict[str, typing.Any]]
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
