""" 
Basic example of scraping pipeline using SmartScraper
"""

import os
from dotenv import load_dotenv
from scrapegraphaisub.graphs import SmartScraperGraph

load_dotenv()
openai_key = os.getenv("OPENAI_APIKEY")

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "gpt-3.5-turbo",
    },
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the news with their description.",
    file_source="/Users/marcovinciguerra/Github/Scrapegraph-ai/examples/graph_examples/plain_html_example.txt",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
