# GOAL

This is a project meant for me to learn and practice with:

- FrontEnd
  - React
  - TypeScript
  - PWA
- BackEnd
  - Python FastAPI
  - (future) migrate python backend to Go
- Database
  - PostgreSQL
- Authentication
  - Email/Password
  - OAuth2 (Google, GitHub, etc.)
  - Goal of 2 account to start with, but will expand to more in the future
- Real-Time Communication
  - WebSockets
- Notifications
  - Email
  - Push Notifications (PWA)
  - triggerable base on user preferences
- Hosting
  - Docker
  - (future) Kubernetes
  - VPS
- CI/CD
  - GitHub Actions
- Testing
  - Unit Testing
  - Integration Testing
  - End-to-End Testing (Vitest/Playwright)

## The project is to make a task tracker meant for my household. The goal is to have a simple and easy to use task tracker that can be used by my family members to keep track of tasks that need to be done around the house

## Development Environment Setup

This guide installs and configures everything required to develop and run the
Household Tasks project locally.

## 1. Install required software

Install these in this order.

### 1.1 WSL 2

Docker Desktop on Windows uses WSL 2 by default.

Open PowerShell as Administrator and run:

```powershell
wsl --install
```

Restart your computer when prompted.

After restarting, open Ubuntu and create a Linux username and password.

Verify WSL:

```powershell
wsl --version
```

Docker Desktop requires WSL 2.1.5 or later; using the latest version is
recommended. [Docker Docs](https://docs.docker.com/desktop/setup/install/windows-install/)

### 1.2 Docker Desktop

Download Docker Desktop:

https://www.docker.com/products/docker-desktop/

Install it and select **Use WSL 2 instead of Hyper-V** if prompted.

After installation:

1. Start Docker Desktop.
2. Accept the service agreement.
3. Go to **Settings → General**.
4. Ensure **Use the WSL 2 based engine** is enabled.
5. Click **Apply & Restart**.

Docker Desktop on Windows supports WSL 2, Hyper-V, and Docker VMM backends;
WSL 2 is the default and works for most users.
[Docker Docs](https://docs.docker.com/desktop/setup/install/windows-install/)

Verify:

```powershell
docker --version
docker compose version
```

Test Docker:

```powershell
docker run hello-world
```

### 1.3 Python

Install Python 3.12 or newer:

https://www.python.org/downloads/

During installation, check:

- **Add Python to PATH**
- **Install pip**

Verify:

```powershell
python --version
pip --version
```

### 1.4 Node.js

Install the current Node.js LTS version:

https://nodejs.org/

Vite requires Node.js 18 or newer; using the latest LTS version is
recommended. [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Frameworks_libraries/React_getting_started)

Verify:

```powershell
node -v
npm -v
```

## 2. Create environment variables

Create a file named:

```text
.env
```

Use `.env.example` as the template:

```powershell
Copy-Item .env.example .env
```

**Important**:

- Never commit `.env`.
- `.env` must remain in `.gitignore`.
- Change all default passwords and secrets before deploying.
- Use a long random value for `JWT_SECRET`.

FastAPI’s OAuth2/JWT setup uses a secret key to sign and verify tokens.
[FastAPI Docs](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## 3. Backend setup

Open a terminal in the project root:

```powershell
cd backend
```

Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install backend dependencies:

```powershell
pip install -r requirements.txt
```

These packages provide:

| Package | Purpose |
| --- | --- |
| `fastapi[standard]` | FastAPI framework, Uvicorn server, and common extras |
| `sqlmodel` | SQL models and database sessions |
| `psycopg[binary]` | PostgreSQL driver |
| `alembic` | Database migrations |
| `pyjwt` | JWT creation and verification |
| `passlib[bcrypt]` | Password hashing |
| `pytest` | Backend tests |
| `httpx` | API test client |

FastAPI’s deployment guidance uses `fastapi[standard]`, SQLModel, Alembic,
and `psycopg[binary]` for a PostgreSQL-backed application.
[Sevalla Docs](https://docs.sevalla.com/guides/python/fastapi/deploy)

## 4. Database setup

From the project root:

```powershell
cd ..
docker compose up -d db
```

Check that PostgreSQL is running:

```powershell
docker compose ps
```

Connect to the database:

```powershell
docker compose exec db psql -U taskuser -d tasks
```

Inside PostgreSQL, run:

```sql
SELECT version();
\q
```

## 5. Run the backend

From the `backend/` folder:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

Open:

```text
http://127.0.0.1:8000/docs
```

## 6. Frontend setup

Open a second terminal in the project root:

```powershell
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
```

Install frontend dependencies:

```powershell
npm install axios react-router-dom
```

Run the frontend:

```powershell
npm run dev
```

Open:

```text
http://localhost:5173
```

Vite’s React TypeScript template creates `main.tsx` and `App.tsx`, with
TypeScript checking configured.
[Coddy Docs](https://coddy.tech/docs/install-react)

## 7. Add PWA support later

Do this only after the basic React app works.

From `frontend/`:

```powershell
npm install -D vite-plugin-pwa
```

The Vite PWA plugin works with React, TypeScript, and Vite, and supports
service workers, caching, installability, and push notifications.
[Vite PWA Docs](https://vite-pwa-org.netlify.app/frameworks/)

## 8. Run everything with Docker later

Once the backend and frontend have Dockerfiles, you will be able to run:

```powershell
docker compose up --build
```

For now, run PostgreSQL and the backend separately while learning.

## 12. Verification checklist

You are ready to start coding when all of these work:

```powershell
git --version
docker --version
docker compose version
python --version
pip --version
node -v
npm -v
```

And:

- Docker Desktop is running.
- PostgreSQL starts with `docker compose up -d db`.
- FastAPI runs at `http://127.0.0.1:8000/docs`.
- React runs at `http://localhost:5173`.
- `.env` exists locally and is ignored by Git.
