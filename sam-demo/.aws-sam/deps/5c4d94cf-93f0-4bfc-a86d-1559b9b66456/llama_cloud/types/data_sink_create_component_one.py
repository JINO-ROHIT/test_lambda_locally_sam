# This file was auto-generated by Fern from our API Definition.

import typing

from .cloud_azure_ai_search_vector_store import CloudAzureAiSearchVectorStore
from .cloud_chroma_vector_store import CloudChromaVectorStore
from .cloud_milvus_vector_store import CloudMilvusVectorStore
from .cloud_mongo_db_atlas_vector_search import CloudMongoDbAtlasVectorSearch
from .cloud_pinecone_vector_store import CloudPineconeVectorStore
from .cloud_postgres_vector_store import CloudPostgresVectorStore
from .cloud_qdrant_vector_store import CloudQdrantVectorStore
from .cloud_weaviate_vector_store import CloudWeaviateVectorStore

DataSinkCreateComponentOne = typing.Union[
    CloudChromaVectorStore,
    CloudPineconeVectorStore,
    CloudPostgresVectorStore,
    CloudQdrantVectorStore,
    CloudWeaviateVectorStore,
    CloudAzureAiSearchVectorStore,
    CloudMongoDbAtlasVectorSearch,
    CloudMilvusVectorStore,
]
