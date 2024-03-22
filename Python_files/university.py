import pandas as pd
from rdflib import Graph, Namespace, Literal, URIRef, XSD
from rdflib.namespace import RDF, RDFS

try:
    df = pd.read_csv("/content/university_data.csv")
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()

g = Graph()

focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)

# Iterate through each row and add triples to the graph
for index, row in df.iterrows():
    university_uri = focu[row['universityName'].replace(" ", "_")]
    g.add((university_uri, RDF.type, focu.University))
    g.add((university_uri, focudata.universityName, Literal(row['universityName'], datatype=XSD.string)))
    g.add((university_uri, focudata.dbpediaLink, URIRef(row['dbpediaLink'])))
    g.add((university_uri, focudata.wikidataLink, URIRef(row['wikidataLink'])))

try:
    g.serialize(destination='university_data.ttl', format='turtle')
    print("RDF serialization successful.")
except Exception as e:
    print(f"Error occurred while serializing RDF: {e}")
