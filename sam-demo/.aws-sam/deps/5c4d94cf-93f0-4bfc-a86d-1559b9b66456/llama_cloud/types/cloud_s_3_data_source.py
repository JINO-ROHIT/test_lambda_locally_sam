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


class CloudS3DataSource(pydantic.BaseModel):
    """
    Base component object to capture class names.
    """

    bucket: str = pydantic.Field(description="The name of the S3 bucket to read from.")
    prefix: typing.Optional[str] = pydantic.Field(description="The prefix of the S3 objects to read from.")
    aws_access_id: typing.Optional[str] = pydantic.Field(description="The AWS access ID to use for authentication.")
    aws_access_secret: typing.Optional[str] = pydantic.Field(
        description="The AWS access secret to use for authentication."
    )
    s_3_endpoint_url: typing.Optional[str] = pydantic.Field(
        alias="s3_endpoint_url", description="The S3 endpoint URL to use for authentication."
    )
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
