# Smart Student Marketplace & Service Platform

## Team Members

| Full Name | Student ID | Email | Main Responsibilities |
|---|---:|---|---|
| Mustafa Ismaili | 131968 | mi31968@seeu.edu.mk | Backend, API, Database, Testing |
| Amra Demiri | 131969 | ad31969@seeu.edu.mk | Frontend, UI/UX, Integration, Documentation |

## Project Description

Smart Student Marketplace & Service Platform is a web application designed for university students. Students can register, log in, post services or items, search listings, send messages, and leave reviews. The goal is to create a more structured and trusted alternative to unorganized social media posts.

## Main Features

- User registration and login
- Service/item posting
- Search and category filtering
- Messaging between students
- Review and rating system
- Unit tests for the main backend logic

## Technologies Used

- Python 3
- Flask
- SQLite
- Pytest
- HTML, CSS, JavaScript
- GitHub for version control

## Project Structure

```text
smart-student-marketplace/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── tests/
│   └── test_app.py
├── docs/
│   └── Project Proposal.pdf
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/smart-student-marketplace.git
cd smart-student-marketplace
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### 5. Run the backend

```bash
python backend/app.py
```

The backend will run on:

```text
http://127.0.0.1:5000
```

### 6. Open the frontend

Open this file in your browser:

```text
frontend/index.html
```

## Running Unit Tests

Install dependencies first, then run:

```bash
pytest
```

The tests check meaningful functionality such as registration, login, service creation, search, messaging, and reviews.

## Version Control Notes

This repository should show regular commits from both team members. Recommended commit examples:

```text
Initial project setup
Add backend database models
Implement authentication API
Add service posting functionality
Create frontend pages
Add search feature
Add unit tests
Update README instructions
```

## Repository Submission

Submit the public GitHub repository link or add the professor as a collaborator.
