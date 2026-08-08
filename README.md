# 💼 Job Board API

A backend API for job listings, companies and applications built with FastAPI and PostgreSQL.

---

## 🚀 What This Project Does

- Register and login securely
- Create and manage companies
- Post job listings with salary range and job type
- Search and filter jobs by keyword, type and location
- Apply to jobs with cover letter
- Track application status (pending, reviewed, accepted, rejected)
- Company owners can view and manage applications

---

## 🧠 What I Learned Building This

- Multiple models with relationships (Company → Job → Application)
- Foreign keys connecting three tables
- Public vs protected endpoints
- Preventing duplicate applications
- Role-based access (company owner vs applicant)
- Enum types for job types and application status
- Salary range with min and max values

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Programming language |
| FastAPI | Web framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Migrations |
| PyJWT | Authentication |
| bcrypt | Password hashing |
| Docker | Containerization |
| Uvicorn | Server |

---

## ⚙️ How To Run

### Without Docker:
```bash
git clone https://github.com/sivamani151dev-cell/job-board.git
cd job-board
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Setup .env file
python -m alembic upgrade head
uvicorn app.main:app --reload
```

### With Docker:
```bash
docker-compose up --build
```

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Register | ❌ |
| POST | `/auth/login` | Login | ❌ |

### Companies
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/companies/` | Create company | ✅ |
| GET | `/companies/` | List all companies | ❌ |
| GET | `/companies/{id}` | Get company | ❌ |
| PUT | `/companies/{id}` | Update company | ✅ |
| DELETE | `/companies/{id}` | Delete company | ✅ |

### Jobs
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/jobs/` | Post a job | ✅ |
| GET | `/jobs/` | List all jobs | ❌ |
| GET | `/jobs/?keyword=x` | Search jobs | ❌ |
| GET | `/jobs/{id}` | Get specific job | ❌ |
| PUT | `/jobs/{id}` | Update job | ✅ |
| DELETE | `/jobs/{id}` | Delete job | ✅ |

### Applications
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/applications/{job_id}` | Apply to job | ✅ |
| GET | `/applications/my` | My applications | ✅ |
| GET | `/applications/job/{id}` | Job applications | ✅ |
| PUT | `/applications/{id}` | Update status | ✅ |
| DELETE | `/applications/{id}` | Withdraw | ✅ |

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key for JWT signing |
| `ALGORITHM` | JWT algorithm (HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time |

---

## 📁 Project Structure

job-board/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── auth.py
│ ├── models/
│ │ ├── user.py
│ │ ├── company.py
│ │ ├── job.py
│ │ └── application.py
│ ├── schemas/
│ │ ├── user.py
│ │ ├── company.py
│ │ ├── job.py
│ │ └── application.py
│ └── routers/
│ ├── auth.py
│ ├── companies.py
│ ├── jobs.py
│ └── applications.py
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md

---

## 🎯 Project Type
Skill-Building Project — built to understand multi-table relationships, role-based access and complex filtering.