def read_and_parse_text(file_path):
    """Read and parse text data from a file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def compare_lines(file1_lines, file2_lines):
    """Compare lines from two files and return differences."""
    differences = []
    max_lines = max(len(file1_lines), len(file2_lines))
    
    for i in range(max_lines):
        line1 = file1_lines[i] if i < len(file1_lines) else ''
        line2 = file2_lines[i] if i < len(file2_lines) else ''
        
        if line1 != line2:
            differences.append((i + 1, line1, line2))
    
    return differences

def main(file1_path, file2_path):
    file1_lines = read_and_parse_text(file1_path)
    file2_lines = read_and_parse_text(file2_path)
    
    differences = compare_lines(file1_lines, file2_lines)
    
    if not differences:
        print("The files are identical.")
    else:
        print("Differences found:")
        for line_num, line1, line2 in differences:
            print(f"Line {line_num}:")
            print(f"File 1: {line1}")
            print(f"File 2: {line2}")
            print()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python comparer.py <file1> <file2>")
        sys.exit(1)
    
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    
    main(file1_path, file2_path)
