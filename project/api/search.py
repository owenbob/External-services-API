"""
Module to hold Elasticsearch connections
"""

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from api.models import Posts

connections.create_connection()

class PostsIndex(DocType):
    id = Text()
    title = Text()
    body = Text()

    class Index:
        name = "post-index"

def bulk_indexing():
    PostsIndex.init()
    es = Elasticsearch()
    import pdb; pdb.set_trace()
    bulk(client=es, actions=(b.indexing() for b in Posts.objects.all().iterator()))

def search(title):
    s = Search().filter('term', title=title)
    response = s.execute()
    return response
