# Read the file containing the grammar
file_path = "sa.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
    # Remove newline character
    line = line[:-1] if line.endswith('\n') else line
    
    # Find the index of the arrow symbol
    arrow_index = 0
    for i, char in enumerate(line):
        if char == "-" and i < len(line) - 1 and line[i+1] == ">":
            arrow_index = i
            break
    
    # Extract non-terminal and production
    non_terminal = line[:arrow_index]
    production = line[arrow_index + 2:]
    
    # Separate rules with left recursion and without left recursion
    rules_with_recursion = []
    rules_without_recursion = []
    current_rule = ""
    
    for char in production:
        if char == "|":
            if current_rule.startswith(non_terminal):
                rules_with_recursion += [current_rule]
            else:
                rules_without_recursion += [current_rule]
            current_rule = ""
        else:
            current_rule += char
    
    if current_rule.startswith(non_terminal):
        rules_with_recursion += [current_rule]
    else:
        rules_without_recursion += [current_rule]
    
    # If there are no rules with left recursion, no transformation is needed
    if not rules_with_recursion:
        print(f"No left recursion found in the production: {production}")
    else:
        new_non_terminal = non_terminal + "'"
        
        # Print the transformed rules
        transformed_rules = []
        for rule in rules_without_recursion:
            transformed_rules += [rule[len(non_terminal):] + new_non_terminal]
        print(f"{non_terminal} -> {' | '.join(transformed_rules)}")
        
        transformed_rules = []
        for rule in rules_with_recursion:
            transformed_rules += [rule[len(non_terminal):] + new_non_terminal]
        print(f"{new_non_terminal} -> {' | '.join(transformed_rules)} | ε")
