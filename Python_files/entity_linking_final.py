from tqdm import tqdm

# Loop through the COMP_474 and COMP_6721 directories
for course_dir in ["COMP_474", "COMP_6721"]:
    course_path = os.path.join(input_dir, course_dir, "lecture_contents")
    output_file = os.path.join(output_dir, f"{course_dir}_automated_topics.txt")

    # Create a list to store the linked entities
    linked_entities = []

    # Loop through the lecture directories
    for lecture_dir in tqdm(sorted(os.listdir(course_path)), desc=f"Processing {course_dir}"):
        lecture_path = os.path.join(course_path, lecture_dir)

        # Check if the directory is a lecture directory
        if os.path.isdir(lecture_path):
            # Loop through the slides and worksheets folders
            for folder in ["slides", "worksheets"]:
                folder_path = os.path.join(lecture_path, folder)
                if os.path.exists(folder_path):
                    # Loop through the .txt files in the folder
                    for filename in os.listdir(folder_path):
                        if filename.endswith(".txt"):
                            file_path = os.path.join(folder_path, filename)
                            with open(file_path, "r", encoding="utf-8") as file:
                                text = file.read()

                            # Process the text using spaCy
                            doc = nlp(text)

                            # Create a list to store the named entities (to maintain order)
                            named_entities = []

                            # Iterate through the entities
                            for ent in doc.ents:
                                # Check if the entity is alphanumeric using a regular expression
                                if re.match(r"^[a-zA-Z0-9]+(?:\s[a-zA-Z0-9]+)*$", ent.text):
                                    # Merge multi-word named entities with underscores
                                    named_entity = "_".join(ent.text.split())
                                    if named_entity not in named_entities:
                                        named_entities.append(named_entity)

                            # Use DBpedia Spotlight to link the named entities
                            for entity in named_entities:
                                base_url = "http://api.dbpedia-spotlight.org/en/annotate"
                                params = {
                                    'text': entity.replace("_", " "),
                                    'confidence': '0.5',
                                    'support': '5'
                                }
                                headers = {'accept': 'application/json'}
                                response = requests.get(base_url, params=params, headers=headers)
                                if response.status_code == 200:
                                    data = response.json()
                                    if 'Resources' in data and len(data['Resources']) > 0:
                                        for resource in data["Resources"]:
                                            linked_entities.append((entity, resource["@URI"], file_path, f"{course_dir}_LECTURE_{lecture_dir.split('_')[1]}"))

    # Save the linked entities to the output file with UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as file:
        for entity, uri, path, course_lec_num in sorted(linked_entities, key=lambda x: x[3]):
            file.write(f"{entity} {uri} {path} {course_lec_num}\n")

    print(f"Linked entities for {course_dir} saved to {output_file}")
