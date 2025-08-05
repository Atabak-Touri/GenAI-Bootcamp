"""
Code Examples: Flask Rules for Junior Developers

This file demonstrates best practices for:
1. Never exposing secret keys or credentials in code
2. Validating and sanitizing all user input
3. Using Flask’s debug mode only in development
"""

# ---------------------------------------------
# 1. Never Expose Secret Keys or Credentials in Code
# ---------------------------------------------

# Bad Practice (do NOT do this):
# from flask import Flask
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'my-very-secret-key'  # ❌ Hardcoded secret

# Good Practice:
import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # ✅ Loaded from environment variable

# ---------------------------------------------
# 2. Validate and Sanitize All User Input
# ---------------------------------------------

# Bad Practice (do NOT do this):
# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form['username']  # ❌ No validation
#     # ... use username directly ...

# Good Practice (using WTForms):
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data  # ✅ Validated and sanitized
        # ... use username safely ...
        return 'Success'
    return render_template('submit.html', form=form)

# ---------------------------------------------
# 3. Use Flask’s Debug Mode Only in Development
# ---------------------------------------------

# Bad Practice (do NOT do this):
# app.run(debug=True)  # ❌ Never do this in production!

# Good Practice:
if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug_mode)