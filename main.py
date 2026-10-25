"""
VoiceRAG root entry point.
Run with:
    uv run python main.py
or:
    uv run uvicorn src.main:app --host localhost --port 8000
"""
import uvicorn
from src.main import app

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )
