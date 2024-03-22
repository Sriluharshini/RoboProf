from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, XSD
import pandas as pd

df = pd.read_csv(r"C:\Users\anmol\Downloads\Intelligent_System_6741\project\merged_file.csv", encoding ='utf-8')
g = Graph()

focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
g.bind("focu", focu)
g.bind("focudata", focudata)

# Create URI for Concordia University
concordia_uri = focudata["Concordia_University"]

# Add triples linking Concordia University to individual courses
course_uris = []
for index, row in df.iterrows():
    course_uri = focudata[f"course_{row['Subject']}_{row['Catalog']}"]
    course_uris.append(course_uri)
    g.add((course_uri, RDF.type, focu.Course))
    g.add((course_uri, focudata.CourseSubject, Literal(row['Subject'])))
    g.add((course_uri, focudata.catalog, Literal(row['Catalog'])))
    g.add((course_uri, focudata.CourseName, Literal(row['Long Title'])))
    g.add((course_uri, focudata.CourseCredits, Literal(row['Class Units'], datatype=XSD.integer)))
    g.add((course_uri, focudata.componentCode, Literal(row['Component Code'])))
    g.add((course_uri, focudata.componentDescr, Literal(row['Component Descr'])))
    g.add((course_uri, focudata.prerequisiteDescr, Literal(row['Pre Requisite Description'])))
    g.add((course_uri, focudata.career, Literal(row['Career'])))
    g.add((course_uri, focudata.equivalentCourses, Literal(row['Equivalent Courses'])))
    g.add((course_uri, focudata.Descr, Literal(row['Descr'])))


# Add triples linking Concordia University to courses
g.add((concordia_uri, focu.hasCourse, course_uris[0]))  # Assuming at least one course exists
for course_uri in course_uris[1:]:
    g.add((concordia_uri, focu.hasCourse, course_uri))

g.serialize(destination='CU_courses_Mapping.ttl', format='turtle')
