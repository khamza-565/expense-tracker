# Expense Tracker CLI

A simple command-line application written in Python for tracking and managing personal expenses.

## Features

- **Add expenses** — add a new expense with a description and amount.
- **List expenses** — display all saved expenses with their IDs, descriptions, and amounts.
- **View total expenses** — calculate and display the total amount of all expenses.
- **Delete expenses** — remove an expense by its ID.
- **Data persistence** — automatically save expenses in a JSON file (`data.json`).
- **Input validation** — prevent empty descriptions, invalid numbers, and amounts less than or equal to zero.
- **Unique IDs** — automatically generate a unique ID for each new expense.
- **JSON validation** — validate loaded data and handle duplicate IDs by keeping the last entry.

## Requirements

- Python 3.8 or higher
- No external libraries required.

The application uses Python standard libraries:
- `json`
- `os`
- `math`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/khamza-565/expense-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd expense-tracker
   ```

## How to Run

Run the application using Python:

```bash
python expense_tracker.py
```

Replace `expense_tracker.py` with the actual name of your Python file if it is different.

## Usage

After starting the application, the following menu will appear:

```text
1. Add Expense
2. List Expenses
3. View Total Expenses
4. Delete Expense
5. Exit
```

Choose an option by entering the corresponding number.

### Example

To add a new expense:

1. Select `1`.
2. Enter an expense description.
3. Enter the expense amount.

The expense will be saved automatically.

To delete an expense, select `4` and enter its ID.

## Data Storage

All expenses are stored in a local JSON file named `data.json`.

Example:

```json
[
    {
        "id": 1,
        "description": "Groceries",
        "amount": 25.5
    },
    {
        "id": 2,
        "description": "Coffee",
        "amount": 4.5
    }
]
```

The `data.json` file is created automatically when the first expense is saved.

## Project Status

Completed as part of the [roadmap.sh Backend Developer Roadmap](https://roadmap.sh/projects/expense-tracker).

