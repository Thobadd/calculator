import os
from flask import Flask, render_template, request
import sympy as sp

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.abspath(os.path.join(base_dir, '..', 'templates'))

app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        user_input = request.form.get('expression', '').strip()
        
        if user_input:
            try:
                expression_str = user_input.replace('^', '**')
                expr = sp.sympify(expression_str)
                
                if expr.is_number:
                    if expr in [sp.zoo, sp.oo, -sp.oo]:
                        result = "Cannot divide by zero"
                    else:
                        res_val = float(expr)
                        result = int(res_val) if res_val.is_integer() else res_val
                else:
                    result = "Invalid input"
                    
            except (sp.SympifyError, TypeError, ValueError, SyntaxError):
                result = "Syntax Error"
                
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
