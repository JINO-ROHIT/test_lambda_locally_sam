# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .managed_ingestion_status import ManagedIngestionStatus

try:
    import pydantic
    if pydantic.__version__.startswith("1."):
        raise ImportError
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PipelineDeployment(pydantic.BaseModel):
    """
    Base schema model containing common database fields.
    """

    id: str = pydantic.Field(description="Unique identifier")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(description="Creation datetime")
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(description="Update datetime")
    status: ManagedIngestionStatus = pydantic.Field(description="Status of the pipeline deployment.")
    started_at: typing.Optional[dt.datetime] = pydantic.Field(description="Time the pipeline deployment started.")
    ended_at: typing.Optional[dt.datetime] = pydantic.Field(description="Time the pipeline deployment finished.")

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
