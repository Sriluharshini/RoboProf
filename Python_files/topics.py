import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Read the CSV file
df = pd.read_csv(r"/content/topics.csv")

# Create an RDF Graph
g = Graph()

# Define namespaces
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)

# Iterate through each row and add triples to the graph
for index, row in df.iterrows():
    subject = focu[row['topicName'].replace(" ", "_")]  # Using topicName as the subject
    g.add((subject, RDF.type, focu.Topic))
    g.add((subject, focudata.topicName, Literal(row['topicName'])))
    g.add((subject, focudata.dbpediaTopicLink, Literal(row['dbpediaTopicLink'])))

# Serialize the graph to a .ttl file
g.serialize(destination='topics.ttl', format='turtle')
