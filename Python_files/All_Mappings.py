from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")

g = Graph()

g.bind("focu", focu)
g.bind("focudata", focudata)

# University to Students done
g.add((focudata.Concordia_University, focu.hasStudent, focudata.Alice_Johnson))
g.add((focudata.Concordia_University, focu.hasStudent, focudata.Jane_Smith))
g.add((focudata.Concordia_University, focu.hasStudent, focudata.John_Doe))

# Courses to Student done
g.add((focudata.course_COMP_474, focu.hasStudent, focudata.Alice_Johnson))
g.add((focudata.course_COMP_6721, focu.hasStudent, focudata.Alice_Johnson))
g.add((focudata.course_COMP_474, focu.hasStudent, focudata.Jane_Smith))
g.add((focudata.course_COMP_6721, focu.hasStudent, focudata.John_Doe))

# Students to Courses done
g.add((focudata.Alice_Johnson, focu.enrolledIn, focudata.course_COMP_474))
g.add((focudata.Alice_Johnson, focu.enrolledIn, focudata.course_COMP_6721))
g.add((focudata.Jane_Smith, focu.enrolledIn, focudata.course_COMP_474))
g.add((focudata.John_Doe, focu.enrolledIn, focudata.course_COMP_6721))


# Lectures to Topics changed to focu done
g.add((focu.lecture_2, focu.hasTopics, focudata.IntroductionToIntelligentSystems,))
g.add((focu.lecture_1, focu.hasTopics, focudata.Knowledge_Representation))
g.add((focu.lecture_3, focu.hasTopics, focudata.Machine_Learning))

# Lectures to Slides
# g.add((focudata.lecture_2, focu.hasTopics, focudata.IntroductionToIntelligentSystems))
# g.add((focudata.lecture_1, focu.hasTopics, focudata.IntroductionToKnowledgeGraphs))
# g.add((focudata.lecture_3, focu.hasTopics, focudata.IntroductionToMachineLearning))

# Topic to Slides done
g.add((focudata.Machine_Learning, focu.hasSlides,focudata.slides06))
g.add((focudata.Knowledge_Representation, focu.hasSlides,focudata.slides03))

# Courses to Topic done
g.add((focudata.course_COMP_6721, focu.hasTopic, focudata.Computer_Vision))
g.add((focudata.course_COMP_6721, focu.hasTopic, focudata.Machine_Learning))
g.add((focudata.course_COMP_474, focu.hasTopic, focudata.Machine_Learning))
g.add((focudata.course_COMP_474, focu.hasTopic, focudata.Knowledge_Representation))
g.add((focudata.course_COMP_474, focu.hasTopic, focudata.Natural_Language_Processing))

# Courses to Lectures done to focu
g.add((focudata.course_COMP_474, focu.hasLectures, focu.lecture_1))
g.add((focudata.course_COMP_474, focu.hasLectures, focu.lecture_2))
g.add((focudata.course_COMP_474, focu.hasLectures, focu.lecture_3))
g.add((focudata.course_COMP_6721, focu.hasLectures, focu.lecture_3))

# Students to University done
g.add((focudata.Alice_Johnson, focu.enrolledAt, focudata.Concordia_University))
g.add((focudata.Jane_Smith, focu.enrolledAt, focudata.Concordia_University))
g.add((focudata.John_Doe, focu.enrolledAt, focudata.Concordia_University))

# Serialize the graph to a file
g.serialize("finale_mappings.ttl", format="turtle")