import pandas as pd
from rdflib import Graph, Namespace, Literal, URIRef, XSD
from rdflib.namespace import RDF, RDFS

# Read the CSV file
try:
    df = pd.read_csv("/content/lecture_data.csv")
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()

# Create an RDF Graph
g = Graph()

focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)

for index, row in df.iterrows():
    lecture_uri = focu[f"lecture_{row['lectureNumber']}"]
    g.add((lecture_uri, RDF.type, focu.Lectures))
    g.add((lecture_uri, focudata.lectureNumber, Literal(row['lectureNumber'], datatype=XSD.integer)))
    g.add((lecture_uri, focudata.lectureName, Literal(row['lectureName'], datatype=XSD.string)))
    g.add((lecture_uri, focudata.Slides, Literal(row['Slides'], datatype=XSD.string)))
    g.add((lecture_uri, focudata.Worksheets, Literal(row['Worksheets'], datatype=XSD.string)))
    g.add((lecture_uri, focudata.Reading, Literal(row['Reading'], datatype=XSD.string)))
    g.add((lecture_uri, focudata.OtherMaterial, Literal(row['OtherMaterial'], datatype=XSD.string)))
    g.add((lecture_uri, focudata.lectureWebpage, URIRef(row['lectureWebpage'])))

# Serialize the graph to a .ttl file
try:
    g.serialize(destination='lecture_data.ttl', format='turtle')
    print("RDF serialization successful.")
except Exception as e:
    print(f"Error occurred while serializing RDF: {e}")
