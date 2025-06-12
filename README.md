# Exercise 1 – Project Summary
 
 
##  What We Did (Steps)
 
1. **Created the GitHub repo** – `Excercise-1`.
2. **Made folders** for frontend and backend.
3. **Installed required packages** – `fastapi`, `uvicorn`.
4. **Used Git** for version control and pushed code with proper commit messages.
 
 
---
 
##  Work Division
 
| Part     | Done By     |
| -------- | ----------- |
| Frontend | Saima       |
| Backend  | Chandrakant |
 
 
---
 
##  Folder Structure
 
```
Excercise-1/
│
├── backend/
│   └── main.py
├── frontend/
│   └── interface.py
├── README.md
```
 
---
 
## How to Run
 
### 1. Install Required Packages
 
Make sure Python 3 is installed, then install the following:
 
```bash
pip install fastapi uvicorn
```
 
### 2. Run the Backend Server
 
Navigate to the backend folder and run:
 
```bash
uvicorn main:app --reload
```
 
This will start the FastAPI server at `http://127.0.0.1:8000`
 
### 3. Run the Frontend Script
 
In a separate terminal, run the frontend script:
 
```bash
python frontend/index.html
```
 
---
