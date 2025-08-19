# Todo List App - Copilot Instructions

## Project Overview
This is a simple full-stack todo list application built with FastAPI (backend) and React TypeScript (frontend).

## Architecture
- **Backend**: FastAPI with in-memory storage
- **Frontend**: React with TypeScript and Vite
- **API**: RESTful endpoints for CRUD operations

## Key Features
- Add new todos with title and description
- Mark todos as complete/incomplete
- Edit existing todos
- Delete todos
- Real-time updates between frontend and backend

## API Endpoints
- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo

## Development Setup
1. **Backend**: `cd backend && pip install -r requirements.txt && python -m uvicorn app.main:app --reload`
2. **Frontend**: `cd frontend && npm install && npm run dev`

## Code Style Guidelines
- Use TypeScript for type safety
- Follow React hooks patterns
- Keep components simple and focused
- Use async/await for API calls
- Handle errors gracefully
- Use semantic HTML and accessible patterns

## Common Tasks
- Adding new API endpoints: Update `main.py` and corresponding frontend functions
- Styling: Modify the inline styles in `index.html` or add CSS files
- State management: Currently using React useState, consider Context API for complex state
- Persistence: Currently in-memory, consider adding database integration

## Testing Approach
- Manual testing through the UI
- API testing with tools like Postman or curl
- Consider adding unit tests for components and API endpoints

When making changes, ensure both frontend and backend remain in sync and maintain the simple, clean architecture.