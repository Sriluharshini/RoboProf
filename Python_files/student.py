import pandas as pd
from rdflib import Graph, Namespace, Literal,XSD
from rdflib.namespace import RDF, RDFS


# Read the CSV file
df = pd.read_csv(r"/content/student_data.csv")


# Create an RDF Graph
g = Graph()


focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)


# Iterate through each row and add triples to the graph
for index, row in df.iterrows():
   subject = focu[f"{row['FirstName']}_{row['LastName']}"]
   g.add((subject, RDF.type, focu.Student))
   g.add((subject, focudata.firstName, Literal(row['FirstName'])))
   g.add((subject, focudata.lastName, Literal(row['LastName'])))
   g.add((subject, focudata.studentID, Literal(row['StudentID'], datatype=XSD.integer)))
   g.add((subject, focudata.studentEmail, Literal(row['Email'])))
   g.add((subject, focudata.completedCourses, Literal(row['CompletedCourses'])))
   g.add((subject, focudata.studentGrades, Literal(row['Grades'])))
   g.add((subject, focudata.competencyTopics, Literal(row['Competencies'])))

# Serialize the graph to a .ttl file
g.serialize(destination='student.ttl', format='turtle')
