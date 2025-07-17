#!/usr/bin/env python3
"""
Daily quote updater script
Updates daily.md with a random quote from quotes.txt
"""

import random
import datetime
from pathlib import Path

def get_random_quote():
    """Get a random quote from quotes.txt"""
    quotes_file = Path(__file__).parent / "quotes.txt"
    
    with open(quotes_file, 'r', encoding='utf-8') as f:
        quotes = [line.strip() for line in f if line.strip()]
    
    return random.choice(quotes)

def update_daily_md():
    """Update daily.md with today's quote"""
    quote_line = get_random_quote()
    
    # Split quote and author
    if ' — ' in quote_line:
        quote, author = quote_line.rsplit(' — ', 1)
    else:
        quote = quote_line
        author = "Unknown"
    
    # Get current date
    today = datetime.date.today().strftime("%B %d, %Y")
    
    # Create the content
    content = f"""# Daily Quote

*Updated: {today}*

---

> {quote}

*— {author}*
"""
    
    # Write to daily.md
    daily_file = Path(__file__).parent / "daily.md"
    with open(daily_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated daily.md with quote by {author}")

if __name__ == "__main__":
    update_daily_md()