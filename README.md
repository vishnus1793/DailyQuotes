# Daily Quotes

A simple project that automatically updates with a daily inspirational quote.

## Files

- `daily.md` - The main file that displays today's quote
- `quotes.txt` - Collection of quotes to choose from
- `update.py` - Python script that selects and updates the daily quote
- `.github/workflows/daily.yml` - GitHub Actions workflow for automated daily updates

## How it works

1. The `update.py` script randomly selects a quote from `quotes.txt`
2. It updates `daily.md` with the new quote and current date
3. GitHub Actions runs this script daily via scheduled workflow
4. Changes are automatically committed back to the repository

## Setup

### Local testing
```bash
python update.py
```

### GitHub Actions
The workflow is already configured to run daily at 9 AM UTC. You can also trigger it manually:
1. Go to your GitHub repository → Actions tab
2. Select "Daily Quote Update" workflow
3. Click "Run workflow" button

## Adding quotes

Simply add new quotes to `quotes.txt` in the format:
```
Your quote here — Author Name
```

Each quote should be on its own line.# DailyQuotes
