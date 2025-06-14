
## Backend – FastAPI

This is a basic FastAPI backend with one root endpoint and a Pydantic model.

### Requirements

* Python 3.7 or higher

### Setup Instructions

1. **Navigate to the Backend directory:**

   ```bash
   cd Backend
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirement.txt
   ```

4. **Run the server:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Open in browser:**

   * Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   * Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Project Structure

```
Backend/
├── main.py
├── requirement.txt
└── venv/  (optional, should be in .gitignore)
```


