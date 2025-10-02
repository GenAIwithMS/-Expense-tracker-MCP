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
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/genaiwithms/expense-tracker-mcp.git
cd expense-tracker-mcp
```

2. Install dependencies:
```bash
pip install fastmcp
```

3. Run the server:
```bash
python main.py
```

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
