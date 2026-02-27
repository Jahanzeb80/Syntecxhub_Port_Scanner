# Syntecxhub Port Scanner

A fast and simple Python tool to check for open ports on any website or IP address. This project was built for my Cyber Security internship at Syntecxhub.

## What this tool does
Fast Scanning:     Uses threading to check many ports at the same time.
Single or Range:   You can scan one port (80) or a range (20-100).
Automatic Logging: Saves all results to a file called `scan_results.log`.
Smart Handling:    Handles timeouts and wrong addresses without crashing.

## How to use it
1. Download the `main.py` file.
2. Make sure to install required libraries
3. Open your terminal or command prompt.
4. Run the script:
   ```bash
   python main.py
