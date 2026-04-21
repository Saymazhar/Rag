Secrets folder

Place your runtime-only secret files here (for local development). Do NOT commit actual secret files to git.

Steps:
1. Copy `.env.template` to `.env`.
2. Open `.env` and replace `your_groq_api_key_here` with your actual key.
3. Keep `.env` private — it's ignored by `.gitignore`.

Loading in Python:

```python
from dotenv import load_dotenv
import os
load_dotenv()  # loads .env from current working directory
key = os.getenv("GROQ_API_KEY")
```
