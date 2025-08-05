# Flask Rules for Junior Developers

1. **Never Expose Secret Keys or Credentials in Code**  
   Always keep sensitive information like `SECRET_KEY`, database passwords, and API keys out of your source code. Use environment variables or a separate configuration file (excluded from version control) to manage secrets.

2. **Validate and Sanitize All User Input**  
   Never trust data coming from users. Always validate and sanitize input to prevent security vulnerabilities such as SQL injection, XSS, and CSRF attacks. Use Flask’s built-in request parsing and validation libraries like `wtforms` or `marshmallow`.

3. **Use Flask’s Debug Mode Only in Development**  
   Never run your Flask app with `debug=True` in production. Debug mode can expose sensitive information and allow code execution on your server. Always set `debug=False` (or remove it) and use proper production-ready servers like Gunicorn or uWSGI when deploying.