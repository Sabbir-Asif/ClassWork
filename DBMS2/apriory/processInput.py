def process_input(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    processed_lines = []

    for i, line in enumerate(lines, start=1):
        items = line.strip().split()
        processed_line = f'T{i} ' + ' '.join(f'I{item}' for item in items)
        processed_lines.append(processed_line)

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(processed_lines))

# Example usage:
input_file_path = 'input4.txt'
output_file_path = 'input500.txt'
process_input(input_file_path, output_file_path)
