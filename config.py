"""
Global configuration for README_Agent.
"""
import os
from dotenv import load_dotenv

load_dotenv()

TARGET_REPO = os.getenv("DEFAULT_TARGET_REPO")
MODEL = os.getenv("DEFAULT_MODEL", "gemini-2.5-flash")
MODE = os.getenv("DEFAULT_MODE", "portfolio")

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")
OUTPUT_FILENAME = os.getenv("OUTPUT_FILENAME", "README.generated.md")
