import os
from flask import Flask, render_template, request
import sympy as sp

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.abspath(os.path.join(base_dir, '..', 'templates'))

app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    expression_str = ""
    
    if request.method == 'POST':
        user_input = request.form.get('expression', '').strip()
        expression_str = user_input
        
        if user_input:
            try:
                calc_str = user_input.replace('^', '**')
                calc_str = calc_str.replace('π', 'pi')
                
                expr = sp.sympify(calc_str)
                
                if expr.is_number:
                    if expr in [sp.zoo, sp.oo, -sp.oo] or sp.im(expr) != 0:
                        if sp.im(expr) != 0:
                            result = "Math Error (Complex)"
                        else:
                            result = "Cannot divide by zero"
                    else:
                        res_val = float(expr.evalf())
                        result = int(res_val) if res_val.is_integer() else round(res_val, 8)
                else:
                    result = "Invalid input"
                    
            except (sp.SympifyError, TypeError, ValueError, SyntaxError):
                result = "Syntax Error"
                
    return render_template('index.html', result=result, expression=expression_str)

if __name__ == '__main__':
    app.run(debug=True)
