from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Create a new RDF graph
g = Graph()

# Define namespaces
ns = Namespace("http://namespacetopic.org/")
dbp = Namespace("http://dbpedia.org/resource/")
g.bind("ex", ns)
g.bind("dbp", dbp)

# Read the TXT file and process each line
with open(r"C:\Users\anmol\Downloads\Intelligent_System_6741\build2\data_dir\automated_topics\COMP_474_automated_topics.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")  # Split the line into parts
        if len(parts) >= 3:
            topic_name = parts[0]
            dbpedia_link = parts[1]
            source = " ".join(parts[2:])

            # Create RDF triples
            topic_uri = ns[topic_name.replace(" ", "_")]  # Create URI for topic
            g.add((topic_uri, RDF.type, ns["Topic"]))
            g.add((topic_uri, RDFS.label, Literal(topic_name)))
            g.add((topic_uri, ns["dbpedia_link"], URIRef(dbpedia_link)))
            g.add((topic_uri, ns["source"], Literal(source)))

# Serialize RDF graph to TTL file
g.serialize(destination=r"C:\Users\anmol\Downloads\Intelligent_System_6741\build2\data_dir\automated_topics\triplification_474.ttl", format="turtle")
