""" 
Example of graph builder
"""
import os
from dotenv import load_dotenv
from scrapegraphaisub.builders import GraphBuilder

load_dotenv()
openai_key = os.getenv("OPENAI_APIKEY")

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "gpt-3.5-turbo",
    },
}

# Example usage of GraphBuilder
graph_builder = GraphBuilder(
    user_prompt="Extract the news and generate a text summary with a voiceover.",
    config=graph_config
)

graph_json = graph_builder.build_graph()

# Convert the resulting JSON to Graphviz format
graphviz_graph = graph_builder.convert_json_to_graphviz(graph_json)

# Save the graph to a file and open it in the default viewer
graphviz_graph.render('scrapegraphaisub_generated_graph', view=True)
