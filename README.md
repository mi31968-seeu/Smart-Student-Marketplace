# Smart Student Marketplace & Service Platform

## Project Overview

Smart Student Marketplace & Service Platform is a web application created by Mustafa Ismaili and Amra Demiri. The purpose of the platform is to help university students find and offer trusted student services in one organized place.

Students can use the platform to post services, search for available offers, contact other students, and leave reviews. The project is focused on making student services easier to find compared to unstructured social media posts or group chats.

## Team Members

- Mustafa Ismaili
- Amra Demiri

## Main Features

- User registration and login
- Service posting
- Search and filtering for services
- Messaging between students
- Review and rating system
- Simple frontend interface
- Backend API for managing users, services, and reviews
- Unit tests for important functionality

## Project Structure

```text
smart-student-marketplace/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── tests/
│   └── test_app.py
│
├── docs/
│   └── Project Proposal.pdf
│
├── README.md
└── .gitignore
```

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Pytest
- GitHub

## Frontend Overview

The frontend contains the main user interface of the platform. It includes the homepage, service cards, search section, and add-service form.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mi31968-seeu/smart-student-marketplace.git
```

### 2. Open the project folder

```bash
cd smart-student-marketplace
```

### 3. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the backend

```bash
python app.py
```

The backend will start locally and provide the API for the project.

### 5. Open the frontend

Open the file below in a browser:

```text
frontend/index.html
```

The frontend can be opened directly in the browser and used to view the project interface.

## Running Unit Tests

From the main project folder, run:

```bash
pytest
```

The unit tests are located in the `tests/` folder. They check important parts of the project such as user handling, service posting, searching, and reviews.

## Contribution

The project was developed by both team members.

Mustafa Ismaili worked mostly on:

- Backend development
- API functionality
- Database logic
- Unit testing

Amra Demiri worked mostly on:

- Frontend design
- User interface
- Integration
- Documentation

## Notes

This project demonstrates a simple full-stack software solution with organized source code, documentation, and testing. It uses GitHub for version control and project sharing.
