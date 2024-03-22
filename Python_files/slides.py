import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Read the CSV file
df = pd.read_csv(r"")  # Update with the path to your CSV file

# Create an RDF Graph
g = Graph()

# Define namespaces
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)

# Iterate through each row and add triples to the graph
for index, row in df.iterrows():
    subject = focu[row['slideName'].replace(' ', '_')]  # Convert slideName to subject URI
    g.add((subject, RDF.type, focu.Slide))  # Assuming Slide is the class for slides
    g.add((subject, focudata.slideName, Literal(row['slideName'])))  # Add slideName as a property
    g.add((subject, focudata.slideURI, Literal(row['slideURI'])))  # Add slideURI as a property

# Serialize the graph to a .ttl file
g.serialize(destination='slides.ttl', format='turtle')
