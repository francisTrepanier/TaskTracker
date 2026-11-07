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

## Interactions

1. User taps “Add task”
2. React validates the form
3. React sends POST /tasks with JSON
4. FastAPI receives the request
5. FastAPI validates the JSON against TaskCreate
6. FastAPI calls get_session()
7. get_session opens a database session
8. create_task() runs
9. SQLModel/SQLAlchemy sends INSERT INTO tasks
10. PostgreSQL saves the row
11. FastAPI converts the Task object to JSON
12. React receives the response
13. React updates the task list
14. FastAPI closes the session
