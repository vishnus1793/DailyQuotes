# Minute Quotes

A project that automatically updates with a new inspirational quote every minute.

## Files

- `daily.md` - The main file that displays the current quote
- `quotes.txt` - Collection of quotes to choose from
- `update.py` - Python script that selects and updates the quote
- `index.html` - HTML frontend that displays quotes with live updates
- `.github/workflows/daily.yml` - GitHub Actions workflow for automated minute updates

## How it works

1. The `update.py` script randomly selects a quote from `quotes.txt`
2. It updates `daily.md` with the new quote and current timestamp
3. GitHub Actions runs this script every minute via scheduled workflow
4. Changes are automatically committed back to the repository

## Setup

### Local testing
```bash
# Test the Python script
python update.py

# View the HTML frontend
# Open index.html in your browser or serve it locally:
python -m http.server 8000
# Then visit http://localhost:8000
```

### GitHub Actions
The workflow is configured to run every minute. You can also trigger it manually:
1. Go to your GitHub repository → Actions tab
2. Select "Minute Quote Update" workflow
3. Click "Run workflow" button

**Note:** Running every minute will generate many commits. Consider using this for testing or demo purposes.

## Frontend Features

The HTML frontend (`index.html`) provides:
- **Live updates**: Quotes change automatically every minute
- **Beautiful design**: Glassmorphism UI with smooth animations
- **Responsive**: Works on desktop and mobile devices
- **Timer**: Shows countdown to next quote update
- **Smooth transitions**: Fade animations between quote changes
- **Auto-pause**: Pauses updates when browser tab is not active

## Adding quotes

Simply add new quotes to `quotes.txt` in the format:
```
Your quote here — Author Name
```

Each quote should be on its own line
