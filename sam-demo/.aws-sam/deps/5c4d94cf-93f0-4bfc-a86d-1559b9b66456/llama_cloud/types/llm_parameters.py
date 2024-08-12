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


class LlmParameters(pydantic.BaseModel):
    """
    Base schema model for BaseComponent classes used in the platform.
    Comes with special serialization logic for types used commonly in platform codebase.
    """

    model_name: typing.Optional[str] = pydantic.Field(description="The name of the model to use for retrieval.")
    system_prompt: typing.Optional[str] = pydantic.Field(description="The system prompt to use for the model.")
    temperature: typing.Optional[float] = pydantic.Field(description="The temperature value for the model.")
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
