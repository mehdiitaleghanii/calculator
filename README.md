# Calculator API

Simple calculator API built with FastAPI.

## Setup

Install dependencies:
```bash
pip install -e .
```

## Running

Start the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`.

## Linting and Type Checking

Run ruff for linting:
```bash
uv run ruff check .
```

Run mypy for type checking:
```bash
uv run mypy main.py
```

Run both:
```bash
uv run ruff check . && uv run mypy main.py
```

## Endpoints

- `GET /` - Root endpoint
- `POST /add` - Addition
- `POST /subtract` - Subtraction
- `POST /multiply` - Multiplication
- `POST /divide` - Division

## Using with Insomnia

### 1. Root Endpoint (GET)
- **Method:** `GET`
- **URL:** `http://localhost:8000/`
- **Body:** None

### 2. Add
- **Method:** `POST`
- **URL:** `http://localhost:8000/add`
- **Body Type:** `JSON`
- **Body:**
```json
{
  "a": 10,
  "b": 5
}
```

### 3. Subtract
- **Method:** `POST`
- **URL:** `http://localhost:8000/subtract`
- **Body Type:** `JSON`
- **Body:**
```json
{
  "a": 10,
  "b": 3
}
```

### 4. Multiply
- **Method:** `POST`
- **URL:** `http://localhost:8000/multiply`
- **Body Type:** `JSON`
- **Body:**
```json
{
  "a": 4,
  "b": 7
}
```

### 5. Divide
- **Method:** `POST`
- **URL:** `http://localhost:8000/divide`
- **Body Type:** `JSON`
- **Body:**
```json
{
  "a": 20,
  "b": 4
}
```

## Response Format

All calculation endpoints return:
```json
{
  "result": 15
}
```

**Note:** Division by zero returns a `400 Bad Request` error with message: `"Division by zero is not allowed"`

## Interactive Docs

Visit `http://localhost:8000/docs` for Swagger UI documentation.

