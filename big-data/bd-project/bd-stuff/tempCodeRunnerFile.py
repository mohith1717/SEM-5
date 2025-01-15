import json

# Function to read and sort JSON data from a text file
def read_and_sort_text(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line.strip()) for line in file if line.strip()]
    return sorted(data, key=lambda x: x['city'])

# File paths
output_file = './comp1.txt'
reference_file = './comp2.txt'

# Read and sort both datasets
output_data = read_and_sort_text(output_file)
reference_data = read_and_sort_text(reference_file)

# Compare
if output_data == reference_data:
    print("The outputs match.")
else:
    print("The outputs do not match.")

    # Print differences
    output_dict = {item['city']: item for item in output_data}
    reference_dict = {item['city']: item for item in reference_data}
    
    # Find discrepancies
    all_cities = set(output_dict.keys()).union(reference_dict.keys())
    for city in all_cities:
        output_entry = output_dict.get(city)
        reference_entry = reference_dict.get(city)
        if output_entry != reference_entry:
            print(f"Difference for city {city}:")
            print(f"Output: {output_entry}")
            print(f"Reference: {reference_entry}")
            print()
            
            
            