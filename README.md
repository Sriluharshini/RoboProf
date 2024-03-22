Roboprof, an intelligent agent that can answer university course- and student-related questions, using a knowledge graph and natural language processing

The project folder RoboProf consists of 
1. Vocabulary.ttl file - 
	This covers the schema of the knowledge graph and includes definitions of classes, subclasses, properties between the classes and attributes.
2. Knowledge_Base.ttl file - 
	This holds the total knowledge base for our agent. The file typically consists of all the courses of Concordia University, their details and mapping to the university class, populated data for all the classes used and their inter-class relationships.
3. Dataset folder - 
	This folder typically consists of all the CSV files, slides and lecture data needed to populate the graph.
4. Python_files folder - 
	This folder has all the .py files for populating the data for building the knowledge graph.
5. Intermediate_files_folder - 
	This folder stores all the .ttl files populated by the Python codes from the above folder.
6. Queries folder - 
	This folder consists of all the SPARQL queries specifically created to test and query the agent's knowledge base.

Execution Steps:
1. Run the Apache-fuseki server and upload the Knowledge_Base.ttl file. 
2. Click on the query tab above and run the queries given in the queries folders.
3. Check and compare the results with the knowledge graph and refer vocabulary graph for detailed information on the relationships.

The procedure followed for populating the intermediate TTL files:
1. Open the respective Python code, and provide the path of the CSV or slide data correctly.
2. Specify the destination path and filename.
3. Run the code to populate data.
4. Similarly, follow the steps for courses, students, topics etc; codes.
5. Merge all the TTL files to populate the main Knowledge_Base graph.
