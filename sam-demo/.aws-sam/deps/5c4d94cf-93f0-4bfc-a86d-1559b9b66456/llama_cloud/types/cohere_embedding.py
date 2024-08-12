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


class CohereEmbedding(pydantic.BaseModel):
    """
    CohereEmbedding uses the Cohere API to generate embeddings for text.
    """

    model_name: typing.Optional[str] = pydantic.Field(description="The name of the embedding model.")
    embed_batch_size: typing.Optional[int] = pydantic.Field(description="The batch size for embedding calls.")
    callback_manager: typing.Optional[typing.Dict[str, typing.Any]]
    num_workers: typing.Optional[int] = pydantic.Field(
        description="The number of workers to use for async embedding calls."
    )
    api_key: str = pydantic.Field(description="The Cohere API key.")
    truncate: str = pydantic.Field(description="Truncation type - START/ END/ NONE")
    input_type: typing.Optional[str] = pydantic.Field(
        description="Model Input type. If not provided, search_document and search_query are used when needed."
    )
    embedding_type: str = pydantic.Field(
        description="Embedding type. If not provided float embedding_type is used when needed."
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
        json_encoders = {dt.datetime: serialize_datetime}
