# Job Portal API (Django REST Framework)

A simple Job Portal REST API built with **Django** and **Django REST Framework** that supports:

✅ JWT Authentication  
✅ Applicant CRUD Operations  
✅ Admin Dashboard via Django Admin  
✅ API Browsable Interface via DRF  

This project was done as part of a **Backend Development Assignment**.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| Create Applicant | Anyone can submit job applications |
| View Applicants | List all applicants (secured by JWT) |
| Update Applicant | Update applicant details (JWT required) |
| Delete Applicant | Remove applicant records (JWT required) |
| Authentication | Secure routes using JWT tokens |
| Django Admin | Manage applicants using admin panel |

---

## 🛠️ Tech Stack

- Python (3.13+)
- Django (5.2.7)
- Django REST Framework (3.16.1)
- Simple JWT Authentication (5.5.1)
- SQLite Database

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/gandharvtalikoti/job-portal-api
cd job-portal-api
````

### 2️⃣ Create & Activate Virtual Environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the Server

```bash
python manage.py runserver
```

API will start on:
➡️ [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Authentication (JWT)

### Get Access & Refresh Token

```http
POST /api/auth/login/
Content-Type: application/json
```

Request Body:

```json
{
  "username": "admin",
  "password": "adminpassword"
}
```

Response:

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

Use the **access token** in every authenticated API request:

```http
Authorization: Bearer <access_token>
```

---

## 👨‍💼 Admin Panel Access

Create admin user:

```bash
python manage.py createsuperuser
```

Visit:
➡️ [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📌 API Endpoints

| Method    | Endpoint                | Description              | Auth Required |
| --------- | ----------------------- | ------------------------ | ------------- |
| POST      | `/api/applicants/`      | Create new applicant     | ❌ No          |
| GET       | `/api/applicants/`      | List applicants          | ✅ Yes         |
| GET       | `/api/applicants/{id}/` | Retrieve specific record | ✅ Yes         |
| PUT/PATCH | `/api/applicants/{id}/` | Update applicant         | ✅ Yes         |
| DELETE    | `/api/applicants/{id}/` | Delete applicant         | ✅ Yes         |
| POST      | `/api/auth/login/`      | Get JWT tokens           | ❌ No          |
| POST      | `/api/auth/refresh/`    | Refresh token            | ❌ No          |

---

## 🧪 Database Schema

| Field      | Type              | Description            |
| ---------- | ----------------- | ---------------------- |
| id         | Integer (Auto)    | Primary Key            |
| name       | String            | Applicant Full Name    |
| email      | String            | Unique Email           |
| phone      | String (Optional) | Phone Number           |
| resume     | URL (Optional)    | Resume URL             |
| applied_on | DateTime          | Auto-created timestamp |

---

## ✅ Successful Test Workflow

1. Login → Copy access token
2. Create applicant (public)
3. Fetch applicants (with Authorization header)
4. Update / Delete with token
5. Check data in **Admin Panel**

Everything works ✅

---

## 📄 License

This project is for educational / assignment purpose only.

---

## ✨ Author

**Gandharv Talikoti**
Backend & Machine Learning Engineer
GitHub: [https://github.com/gandharvtalikoti](https://github.com/gandharvtalikoti)


```markdown
# 🧪 API Testing Guide

This document explains how **basic API tests** are implemented and how to run them for the Job Portal API.

---

## ✅ Overview

The project includes simple automated API tests written using **Django REST Framework’s built-in testing tools**.

These tests ensure that:
- The API endpoints are working (GET, POST)
- Authentication (JWT) works correctly
- Basic CRUD operations are valid

---

## 📂 Test File Location

```

applications/tests.py

````

---

## ⚙️ Example Test File

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class ApplicantAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="admin123")
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'admin',
            'password': 'admin123'
        })
        self.access_token = response.data['access']

    def test_create_applicant(self):
        url = reverse('applicant-list')
        data = {"name": "Test User", "email": "test@example.com"}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_applicants(self):
        url = reverse('applicant-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
````

---

## ▶️ How to Run Tests

Make sure your virtual environment is active:

```bash
.\.venv\Scripts\activate
```

Then run:

```bash
python manage.py test
```

---

## 🧾 Expected Output

```bash
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.52s

OK
Destroying test database for alias 'default'...
```

✅ If you see `OK`, all tests have passed successfully.

---

## 🧩 Notes

* These are **basic API integration tests**, not full unit tests.
* They verify that main endpoints work with valid JWT authentication.
* You can expand this file to test more endpoints (Jobs, Applications, etc.) in the future.

---

## 👨‍💻 Author

**Gandharv Talikoti**
Backend Developer | Django & AI Enthusiast
GitHub: [gandharvtalikoti](https://github.com/gandharvtalikoti)

````

