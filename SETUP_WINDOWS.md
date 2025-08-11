# 🚀 Windows Setup Guide for BookReview Microservice

## Prerequisites Installation

### 1. Install Python
```powershell
# Download Python from https://www.python.org/downloads/
# During installation, make sure to check "Add Python to PATH"
# Verify installation:
python --version
# or
py --version
```

### 2. Install Git
```powershell
# Download Git from https://git-scm.com/download/win
# Verify installation:
git --version
```

## Project Setup

### 1. Clone Repository
```powershell
git clone https://github.com/7Chethan007/bookreview-microservice.git
cd bookreview-microservice
```

### 2. Create Virtual Environment
```powershell
# Create virtual environment
python -m venv FlaskAppForDevops

# Activate virtual environment
FlaskAppForDevops\Scripts\Activate.ps1

# If execution policy prevents activation, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activation again:
FlaskAppForDevops\Scripts\Activate.ps1

# You should see (FlaskAppForDevops) in your prompt
```

### 3. Install Dependencies
```powershell
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### 4. Run the Application
```powershell
# Set environment variables
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# Run the application
python app.py
```

### 5. Test the Application
```powershell
# Open a new PowerShell window and test endpoints:

# Test welcome endpoint
Invoke-RestMethod -Uri "http://127.0.0.1:5000/" -Method GET

# Test reviews endpoint  
Invoke-RestMethod -Uri "http://127.0.0.1:5000/reviews" -Method GET

# Test status endpoint
Invoke-RestMethod -Uri "http://127.0.0.1:5000/status" -Method GET
```

### 6. Run Tests
```powershell
# Make sure virtual environment is activated
pytest -v
```

## Postman Testing

### Collection Setup
1. Open Postman
2. Create a new collection: "BookReview API"
3. Add these requests:

**Request 1: Welcome**
- Method: GET
- URL: `http://127.0.0.1:5000/`

**Request 2: Get Reviews**
- Method: GET
- URL: `http://127.0.0.1:5000/reviews`

**Request 3: Health Check**
- Method: GET
- URL: `http://127.0.0.1:5000/status`

## Troubleshooting

### Python Not Found
```powershell
# If you get "Python was not found", try:
py --version
# or reinstall Python from https://www.python.org/downloads/
```

### Virtual Environment Activation Issues
```powershell
# If activation fails, change execution policy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Port Already in Use
```powershell
# If port 5000 is busy, kill the process:
netstat -ano | findstr :5000
# Find the PID and kill it:
taskkill /PID <PID_NUMBER> /F
```

## Expected Output

### Flask Application Running
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[::1]:5000
```

### Test Results
```
tests/test_app.py::test_root PASSED
tests/test_app.py::test_reviews PASSED  
tests/test_app.py::test_status PASSED
```
