# Budget

This repo contains files to create and manage a budget. Create a new monthly budget using the `init.py` file, and update an existing month to a new template file using `update.py`. Create the `data/` directory, where budget files will live.

Within the `data.yaml` file created in the new month, place the correct categorical data and run `budget.py` with the month as the command line argument, in the form YYYY-MM. Then, view the output in the `budget.md` file produced in the monthly folder. Backup all budget files to the path specified in `globals.yaml` under `backup_path`; as budgets are "gitignored", assuming that they contain sensitive data, this allows for all of the produced files, including the budget plain text, output, and statements, to be placed in an external location.

