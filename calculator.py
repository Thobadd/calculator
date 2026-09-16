import sympy as sp

print("--- BODMAS Calculator ---")
print("You can use: +, -, *, /, () brackets, and ^ or ** for powers.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter your expression: ").strip()
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    try:
        expression_str = user_input.replace('^', '**')
        expr = sp.sympify(expression_str)
        
        if expr.is_number:
            if expr in [sp.zoo, sp.oo, -sp.oo]:
                print("Output: Cannot divide by zero\n")
            else:
                print(f"Result: {float(expr)}\n")
        else:
            print("Invalid input: Please enter numbers and operators only (no alphabets).\n")
            
    except (sp.SympifyError, TypeError, ValueError, SyntaxError):
        print("Invalid mathematical expression. Check your brackets or operators!\n")
