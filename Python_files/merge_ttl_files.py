import glob

def merge_ttl_files(input_folder, output_file):
    # Create an empty list to store triples
    triples = []

    # Iterate over each TTL file in the input folder
    for ttl_file in glob.glob(input_folder + "/*.ttl"):
        with open(ttl_file, 'r') as file:
            # Read triples from the TTL file and append them to the list
            triples.extend(file.readlines())

    # Write the merged triples to the output file
    with open(output_file, 'w') as output:
        output.writelines(triples)

# Example usage:
input_folder = r"/content/sample_data/input"  #put the path of the folder where all the ttl files that need to merged are residing
output_file = "combined.ttl"
merge_ttl_files(input_folder, output_file)
