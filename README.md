# Minute Quotes

A project that automatically updates with a new inspirational quote every minute.

## Files

- `daily.md` - The main file that displays the current quote
- `quotes.txt` - Collection of quotes to choose from
- `update.py` - Python script that selects and updates the quote
- `.github/workflows/daily.yml` - GitHub Actions workflow for automated minute updates

## How it works

1. The `update.py` script randomly selects a quote from `quotes.txt`
2. It updates `daily.md` with the new quote and current timestamp
3. GitHub Actions runs this script every minute via scheduled workflow
4. Changes are automatically committed back to the repository

## Setup

### Local testing
```bash
python update.py
```

### GitHub Actions
The workflow is configured to run every minute. You can also trigger it manually:
1. Go to your GitHub repository → Actions tab
2. Select "Minute Quote Update" workflow
3. Click "Run workflow" button

**Note:** Running every minute will generate many commits. Consider using this for testing or demo purposes.

## Adding quotes

Simply add new quotes to `quotes.txt` in the format:
```
Your quote here — Author Name
```

Each quote should be on its own line.# DailyQuotes
