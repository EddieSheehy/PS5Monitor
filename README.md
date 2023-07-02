# PS5Monitor

In February of 2021 I started this project, this was to supply to my friends to allow them to buy PS5's the problems I faced with this project is making it so that the webhook would only be called once upon stock being loaded, then would not ping again once stock was gone.

This script was hosted on Heroku which is the reasoning behind having a Procfile and a requirments.txt.

The script ran on Smyths IE and UK then Gamestop IE and UK similtaneously.

## How to run
```bash
python3 PS5_Monitor.py
```

## Example of Discord Webhook
![Here](images/)
