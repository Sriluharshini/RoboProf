import pandas as pd
from rdflib import Graph, Namespace, Literal, URIRef, XSD
from rdflib.namespace import RDF

try:
    df = pd.read_csv("course_data.csv")
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()
print()

g = Graph()

focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)


for index, row in df.iterrows():
    
    course_uri = focudata[f"course_{row['CourseNumber']}"]
    g.add((course_uri, RDF.type, focu.Course))
    g.add((course_uri, focudata.CourseName, Literal(row['CourseName'], datatype=XSD.string)))
    g.add((course_uri, focudata.CourseSubject, Literal(row['CourseSubject'], datatype=XSD.string)))
    g.add((course_uri, focudata.CourseNumber, Literal(row['CourseNumber'], datatype=XSD.string)))
    g.add((course_uri, focudata.CourseCredits, Literal(row['CourseCredits'], datatype=XSD.integer)))
    g.add((course_uri, focudata.CourseDescription, Literal(row['CourseDescription'], datatype=XSD.string)))
    g.add((course_uri, focudata.courseWebpage, URIRef(row['courseWebpage'])))
    g.add((course_uri, focudata.courseOutline, URIRef(row['courseOutline'])))

try:
    g.serialize(destination='course_data.ttl', format='turtle')
    print("RDF serialization successful.")
except Exception as e:
    print(f"Error occurred while serializing RDF: {e}")