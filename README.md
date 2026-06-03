# Time Agent — README

## Overview
A minimal guide to install and run the Time Agent.

## Requirements
- Python 3.10+ (pip available)
- adk CLI installed and configured
- A Google API key (if required by your use case)

## Installation
1. From your project root, install dependencies:
```bash
pip install geopy timezonefinder
```

## Configuration
1. Create a folder named `time_agent` (if it doesn't already exist).
2. Inside `time_agent`, create a file named `.env` with these exact contents:
```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=YOUR_API_KEY
```
Replace `YOUR_API_KEY` with your actual Google API key.

## Run
From the project root, run:
```bash
adk run time_agent
```

## Notes
- Ensure the `.env` file is not committed to version control (add `time_agent/.env` to `.gitignore`).
- If you need Vertex AI, set `GOOGLE_GENAI_USE_VERTEXAI=1` and configure Vertex credentials accordingly.
