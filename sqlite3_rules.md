# SQLite3: 3 Important Rules for Juniors

## 1. Always Use Parameterized Queries to Prevent SQL Injection
Never directly insert user input into SQL statements. Use placeholders and pass values as parameters to avoid security risks.

**Example:**
```python
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

## 2. Commit Transactions Explicitly
After making changes (INSERT, UPDATE, DELETE), always call `conn.commit()` to save your changes. Forgetting to commit may result in lost data.

**Example:**
```python
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
conn.commit()
```

## 3. Close Connections Properly
Always close your database connection when done to free up resources and avoid database locks. Use context managers (`with` statement) for automatic cleanup.

**Example:**
```python
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    # do database operations
# connection is closed automatically here
```