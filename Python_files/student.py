import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Read the CSV file
df = pd.read_csv(r"C:\Users\anmol\Downloads\Intelligent_System_6741\project\student.csv")

# Create an RDF Graph
g = Graph()

# Define namespaces
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)

# Iterate through each row and add triples to the graph
for index, row in df.iterrows():
    subject = focu[f"{row['FirstName']}_{row['LastName']}"]
    g.add((subject, RDF.type, focu.Student))
    # g.add((subject, ex.FirstName, Literal(row['FirstName'])))
    # g.add((subject, ex.LastName, Literal(row['LastName'])))
    g.add((subject, focudata.studentID, Literal(row['studentID'])))
    g.add((subject, focudata.studentEmail, Literal(row['studentEmail'])))
    g.add((subject, focudata.completedCourses, focudata[(row['completedCourses'])]))
    g.add((subject, focudata.courseGrade, Literal(row['courseGrade'])))
    g.add((subject, focudata.competencyTopics, Literal(row['competencyTopics'])))



# Serialize the graph to a .ttl file
g.serialize(destination='final_student.ttl', format='turtle')