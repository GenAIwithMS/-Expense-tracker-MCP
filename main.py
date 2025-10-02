from fastmcp import FastMCP
import os
import sqlite3
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")

mcp = FastMCP("ExpenseTracker")

def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT DEFAULT ''
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS credits(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                note TEXT DEFAULT ''
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS salary_summaries(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                credit_id INTEGER,
                start_date TEXT,
                end_date TEXT,
                original_salary REAL,
                total_expenses REAL,
                updated_salary REAL,
                summary_note TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS custom_salary_summaries(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                summary_text TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

init_db()

@mcp.tool()
def add_expense(date, amount, category, subcategory="", note=""):
    '''Add a new expense entry to the database.'''
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            "INSERT INTO expenses(date, amount, category, subcategory, note) VALUES (?,?,?,?,?)",
            (date, amount, category, subcategory, note)
        )
        return {"status": "ok", "id": cur.lastrowid}

@mcp.tool()
def delete_expense(expense_id):
    '''Delete an expense entry by its ID.'''
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        return {"status": "ok", "deleted": cur.rowcount}

@mcp.tool()
def edit_expense(expense_id, date=None, amount=None, category=None, subcategory=None, note=None):
    '''Edit an existing expense entry by its ID. Only provided fields will be updated.'''
    fields = []
    values = []
    if date is not None:
        fields.append("date = ?")
        values.append(date)
    if amount is not None:
        fields.append("amount = ?")
        values.append(amount)
    if category is not None:
        fields.append("category = ?")
        values.append(category)
    if subcategory is not None:
        fields.append("subcategory = ?")
        values.append(subcategory)
    if note is not None:
        fields.append("note = ?")
        values.append(note)
    if not fields:
        return {"status": "error", "message": "No fields to update."}
    values.append(expense_id)
    with sqlite3.connect(DB_PATH) as c:
        c.execute(f"UPDATE expenses SET {', '.join(fields)} WHERE id = ?", values)
        return {"status": "ok"}

@mcp.tool()
def list_expenses(start_date, end_date):
    '''List expense entries within an inclusive date range.'''
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT id, date, amount, category, subcategory, note
            FROM expenses
            WHERE date BETWEEN ? AND ?
            ORDER BY id ASC
            """,
            (start_date, end_date)
        )
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

@mcp.tool()
def summarize(start_date, end_date, category=None):
    '''Summarize expenses by category within an inclusive date range.'''
    with sqlite3.connect(DB_PATH) as c:
        query = (
            """
            SELECT category, SUM(amount) AS total_amount
            FROM expenses
            WHERE date BETWEEN ? AND ?
            """
        )
        params = [start_date, end_date]
        if category:
            query += " AND category = ?"
            params.append(category)
        query += " GROUP BY category ORDER BY category ASC"
        cur = c.execute(query, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

@mcp.tool()
def add_credit(date, amount, category, note=""):
    '''Add a new credit (income) entry to the database.'''
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            "INSERT INTO credits(date, amount, category, note) VALUES (?,?,?,?)",
            (date, amount, category, note)
        )
        return {"status": "ok", "id": cur.lastrowid}

@mcp.tool()
def list_credits(start_date, end_date):
    '''List credit (income) entries within an inclusive date range.'''
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT id, date, amount, category, note
            FROM credits
            WHERE date BETWEEN ? AND ?
            ORDER BY id ASC
            """,
            (start_date, end_date)
        )
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

@mcp.tool()
def summarize_credits(start_date, end_date, category=None):
    '''Summarize credits by category within an inclusive date range.'''
    with sqlite3.connect(DB_PATH) as c:
        query = (
            """
            SELECT category, SUM(amount) AS total_amount
            FROM credits
            WHERE date BETWEEN ? AND ?
            """
        )
        params = [start_date, end_date]
        if category:
            query += " AND category = ?"
            params.append(category)
        query += " GROUP BY category ORDER BY category ASC"
        cur = c.execute(query, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

@mcp.tool()
def edit_credit(credit_id, date=None, amount=None, category=None, note=None):
    '''Edit an existing credit (income) entry by its ID. Only provided fields will be updated.'''
    fields = []
    values = []
    if date is not None:
        fields.append("date = ?")
        values.append(date)
    if amount is not None:
        fields.append("amount = ?")
        values.append(amount)
    if category is not None:
        fields.append("category = ?")
        values.append(category)
    if note is not None:
        fields.append("note = ?")
        values.append(note)
    if not fields:
        return {"status": "error", "message": "No fields to update."}
    values.append(credit_id)
    with sqlite3.connect(DB_PATH) as c:
        c.execute(f"UPDATE credits SET {', '.join(fields)} WHERE id = ?", values)
        return {"status": "ok"}

@mcp.tool()
def list_categories():
    '''List all categories from the categories.json file.'''
    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    # Read fresh each time so you can edit the file without restarting
    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return f.read()


@mcp.tool()
def save_salary_summary(summary_text):
    '''
    Save a custom salary summary as plain text for future reference.
    The summary_text should be a detailed description (e.g., generated by Claude or another AI).
    '''
    with sqlite3.connect(DB_PATH) as c:
        # Create table if not exists
        c.execute("""
            CREATE TABLE IF NOT EXISTS custom_salary_summaries(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                summary_text TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute(
            "INSERT INTO custom_salary_summaries (summary_text) VALUES (?)",
            (summary_text,)
        )
        return {"status": "ok", "message": "Custom summary saved."}

@mcp.tool()
def list_salary_summaries():
    '''List all custom salary summaries saved as text.'''
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            """
            SELECT id, summary_text, timestamp
            FROM custom_salary_summaries
            ORDER BY timestamp DESC
            """
        )
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

if __name__ == "__main__":
    mcp.run()
