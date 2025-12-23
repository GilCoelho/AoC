import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables globally when package is imported
# This ensures all libraries can access the environment variables
project_root = Path(__file__).parent.parent.parent
env_file = project_root / '.env'

if env_file.exists():
    load_dotenv(env_file)
    print(f"Loaded environment variables from {env_file}")
else:
    print(f"Warning: .env file not found at {env_file}")
