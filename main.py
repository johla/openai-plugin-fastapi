import os
from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

app = FastAPI()
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])


@app.get("/searchresults", summary="Get search results from Azure Cognitive Search by extracting a query from the user input.", operation_id="getInfo")
async def get_searchresults(query: str = None):
    """
    Returns information from ACS based on a query parameter.
    """

    index_name = "index3"

    print("##### Environment variable:", os.environ.get("SEARCH_KEY"))

    # Get the service endpoint and API key from the environment
    endpoint = os.environ.get("SEARCH_ENDPOINT")
    key = os.environ.get("SEARCH_KEY")

    # Create a client
    credential = AzureKeyCredential(key)
    client = SearchClient(endpoint=endpoint,
                        index_name=index_name,
                        credential=credential)
    
    results = client.search(search_text=query)
    return [
        results
    ]

