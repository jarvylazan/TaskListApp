
# Task List App

This is a simple Task List application built using Python and Kivy. It allows users to add, edit, complete, and delete tasks. The application uses a SQLite database and includes unit testing via `pytest` and documentation generated using Sphinx.

## 📦 Installation

1. Clone the repository.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the App

```bash
python main.py
```

## ✅ Running Tests

```bash
pytest --maxfail=1 --disable-warnings -q
```

All unit tests are located in the `tests/` directory.

## 🧾 Building the Documentation

To build the Sphinx HTML documentation:

```bash
cd docs
make html
```

Then open `_build/html/index.html` in your browser to view the docs.

## 📁 Project Structure

```
Assignment4/
├── app/                # Core app files (main.py, logic_layer.py, db_layer.py)
├── docs/               # Sphinx documentation
├── tests/              # Pytest test cases
├── .env                # Environment configuration
├── db_creation.sql     # SQL schema
├── README.md
```

## 🙋‍♂️ Author

Your Name – 2025
