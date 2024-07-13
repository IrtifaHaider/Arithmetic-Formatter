def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 50:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    answers = []
    
    for problem in problems:
        parts = problem.split() #Split each problem string into its components (operands and operator)
        if parts[1] not in ['+', '-']: #Ensure the operator is either + or -
            return "Error: Operator must be '+' or '-'."
        #Ensure that both operands are valid numbers and have at most four digits.
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Collect the operands and operators for formatting later
        first_operands.append(parts[0])
        operators.append(parts[1])
        second_operands.append(parts[2])
        
        #Calculate the Answers
        if show_answers:
            if parts[1] == '+':
                answers.append(str(int(parts[0]) + int(parts[2])))
            else:
                answers.append(str(int(parts[0]) - int(parts[2])))

    # Creating the formatted strings for output
    first_line = ''
    second_line = ''
    dashes_line = ''
    answers_line = ''
    
    #Format each problem to be arranged vertically and side-by-side
    for i in range(len(problems)):
        length = max(len(first_operands[i]), len(second_operands[i])) + 2 #Determine the required width
        first_line += first_operands[i].rjust(length) + '    ' #Right-align the first operand
        second_line += operators[i] + second_operands[i].rjust(length - 1) + '    ' #Right-align the operator with the second operand
        dashes_line += '-' * length + '    ' # Right-align the dashes
        if show_answers:
            answers_line += answers[i].rjust(length) + '    ' #If answers are to be shown, format and add the answer to the answers_line
    
    #Combine the individual lines into a single string
    if show_answers:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes_line.rstrip() + '\n' + answers_line.rstrip()
    else:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes_line.rstrip()

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])) #Doesn't Show Result
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)) #Shows Result
