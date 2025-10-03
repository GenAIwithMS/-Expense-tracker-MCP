# Expense Tracker MCP Server

A Model Context Protocol (MCP) server for personal expense tracking and management. Track your daily expenses, manage income/salary, and get insights into your spending patterns - all through natural language conversations with your AI assistant.

## Features

- 💰 **Expense Management**: Add, edit, delete, and list expenses with categories and subcategories  
- 💵 **Income Tracking**: Record salary and other income sources  
- 📊 **Smart Summaries**: Get spending breakdowns by category and date range  
- 🏷️ **Built-in Categorization**: Predefined categories with subcategories for detailed tracking  
- 📝 **Custom Notes**: Add notes to any transaction for better context  
- 💾 **Local Storage**: All data stored locally in SQLite database  
- 📈 **Salary Summaries**: Save custom financial summaries for reference  

---

## Installation

### Prerequisites

- Python >= 3.13  
- [uv](https://github.com/astral-sh/uv) (recommended package manager)  

If you don’t have `uv`, install it using:  
```bash
pip install uv
```

### Setup

Clone the repository:

```bash
git clone https://github.com/genaiwithms/expense-tracker-mcp.git
cd expense-tracker-mcp
```

Install dependencies:

```bash
uv add fastmcp
```

Run the server:

```bash
python main.py
```

---

## Using Built-in Categories

We provide built-in categories to prevent misinformation and duplication (for example, Claude may write "Food" and "Dining" as separate categories). Using our built-in categories ensures consistency and accuracy in your expense tracking.

**How to use built-in categories with Claude:**

1. Click on the ➕ plus icon where you attach files.
2. Select “Add from expense tracker”.
3. Click on the `categories.json` file.
4. Now you can simply ask Claude:  
   **“Use the categories I attached”**

This will help Claude (or any MCP client) use the correct, consistent categories for your expenses.

---

## Configuration

### Claude Desktop

Add the server to your Claude Desktop configuration file:

- **MacOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Example configuration:

```json
"ExpenseTracker": {
  "command": "absolute \\path\\to\\uv",
  "args": [
    "run",
    "--with",
    "fastmcp",
    "fastmcp",
    "run",
    "\\absolute\\path to \\Expense-tracker-mcp\\main.py"
  ],
  "env": {},
  "transport": "stdio",
  "type": null,
  "cwd": null,
  "timeout": null,
  "description": null,
  "icon": null,
  "authentication": null
}
```

**Important for New Users:**  
Replace `"absolute \\path\\to\\uv"` with the full path to your `uv` binary.  
Replace `"\\absolute\\path to \\Expense-tracker-mcp\\main.py"` with the full path to your `main.py` file inside this project.

If you’re unsure about your `uv` path, run:

Mac/Linux
```bash
which uv
```

on Windows
```powershell
where uv
```

---

## Usage Examples

### Adding Expenses

- "Add an expense of 50 Rs for travel to Sargodha yesterday"
- "I spent 500 on food and 300 on healthcare today"

### Tracking Income

- "I received my salary of 40,000 Rs today"
- "Add a credit of 5000 Rs from freelance work"

### Getting Summaries

- "Show me all my expenses for this month"
- "What's my total food expense for the last week?"
- "Summarize my spending by category"
- "How much salary do I have remaining?"

### Managing Records

- "Edit expense #5 and change the amount to 600"
- "Delete expense #12"
- "Show me all expenses from October 1 to October 10"

---

## Available Tools

### Expenses

- `add_expense` - Add a new expense entry
- `delete_expense` - Delete an expense by ID
- `edit_expense` - Edit an existing expense
- `list_expenses` - List expenses within a date range
- `summarize` - Get expense summary by category

### Income/Credits

- `add_credit` - Add income/salary entry
- `list_credits` - List credits within a date range
- `summarize_credits` - Get income summary by category

### Categories

- `list_categories` - View all available categories and subcategories

---

## Database Schema

The server uses SQLite with the following tables:

- **expenses:** id, date, amount, category, subcategory, note
- **credits:** id, date, amount, category, note

---

## Development

### Project Structure

```
expense-tracker-mcp/
├── main.py              # MCP server implementation
├── categories.json      # Category definitions
├── expenses.db          # SQLite database (auto-created)
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

### Adding Custom Categories

Edit `categories.json` to add or modify expense categories and subcategories.

---

## Privacy & Security

- All data is stored locally on your machine
- No data is sent to external servers
- Database file is created in the project directory
- Suitable for personal financial tracking

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## License

This project is open source and available under the MIT License.

---

## Acknowledgments

Built with FastMCP - A Python framework for building MCP servers.

---

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

> **Note:** This MCP server is designed for personal use. Always keep backups of your `expenses.db` file to prevent data loss.
