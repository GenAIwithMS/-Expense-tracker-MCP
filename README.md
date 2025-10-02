# Expense Tracker MCP Server

A Model Context Protocol (MCP) server for personal expense tracking and management. Track your daily expenses, manage income/salary, and get insights into your spending patterns - all through natural language conversations with your AI assistant.

## Features

- 💰 **Expense Management**: Add, edit, delete, and list expenses with categories and subcategories
- 💵 **Income Tracking**: Record salary and other income sources
- 📊 **Smart Summaries**: Get spending breakdowns by category and date range
- 🏷️ **Categorization**: 20+ predefined categories with subcategories for detailed tracking
- 📝 **Custom Notes**: Add notes to any transaction for better context
- 💾 **Local Storage**: All data stored locally in SQLite database
- 📈 **Salary Summaries**: Save custom financial summaries for reference

## Categories Supported

- Food & Dining
- Transport
- Housing
- Utilities
- Health
- Education
- Family & Kids
- Entertainment
- Shopping
- Subscriptions
- Personal Care
- Gifts & Donations
- Finance & Fees
- Business
- Travel
- Home
- Pet
- Taxes
- Investments
- Miscellaneous

Each category includes relevant subcategories for detailed expense tracking.

## Installation

### Prerequisites

- Python >= 3.13
- [uv](https://github.com/astral-sh/uv) (for dependency management)

If you don’t already have `uv`, install it with:
'''bash
pip install uv'''


### Setup

1. Clone the repository:
'''bash
git clone https://github.com/genaiwithms/expense-tracker-mcp.git
cd expense-tracker-mcp'''


2. Install dependencies:
'''bash
uv add fastmcp'''

3. Run the server:
'''bash
python main.py
'''

## Configuration

### Claude Desktop

Add the server to your Claude Desktop configuration file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "expense-tracker": {
      "command": "python",
      "args": [
        "/absolute/path/to/expense-tracker-mcp/main.py"
      ]
    }
  }
}
```

### Other MCP Clients

For other MCP-compatible clients, use the stdio transport and point to the `main.py` file.

## Usage Examples

### Adding Expenses

"Add an expense of 50 Rs for travel to Sargodha yesterday"

"I spent 500 on food and 300 on healthcare today"

### Tracking Income

"I received my salary of 40,000 Rs today"

"Add a credit of 5000 Rs from freelance work"

### Getting Summaries

"Show me all my expenses for this month"

"What's my total food expense for the last week?"

"Summarize my spending by category"

"How much salary do I have remaining?"

### Managing Records

"Edit expense #5 and change the amount to 600"

"Delete expense #12"

"Show me all expenses from October 1 to October 10"

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
- `edit_credit` - Edit an existing credit entry

### Categories & Summaries
- `list_categories` - View all available categories and subcategories
- `save_salary_summary` - Save a custom financial summary
- `list_salary_summaries` - View saved financial summaries

## Database Schema

The server uses SQLite with the following tables:

- **expenses**: id, date, amount, category, subcategory, note
- **credits**: id, date, amount, category, note
- **custom_salary_summaries**: id, summary_text, timestamp

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

## Privacy & Security

- All data is stored locally on your machine
- No data is sent to external servers
- Database file is created in the project directory
- Suitable for personal financial tracking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

Built with [FastMCP](https://github.com/jlowin/fastmcp) - A Python framework for building MCP servers.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Note**: This MCP server is designed for personal use.
