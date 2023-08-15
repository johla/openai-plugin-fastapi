import os
from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

app = FastAPI()
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])


@app.get("/info", summary="Get information from Azure cognitive search by extracting a query from the ", operation_id="getInfo")
async def get_info(query: str = None):
    """
    Returns information based on a query parameter.
    """

    index_name = "index3"
    # Get the service endpoint and API key from the environment
    endpoint = os.environ["search-endpoint"]
    key = os.environ["search-key"]

    # Create a client
    credential = AzureKeyCredential(key)
    client = SearchClient(endpoint=endpoint,
                        index_name=index_name,
                        credential=credential)
    
    results = client.search(search_text=query)
    return [
        results
    ]

