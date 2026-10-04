# 🐦 ChirpSocialNetwork

ChirpSocialNetwork is a small Twitter-like social network developed in Python as a practical exercise in Object-Oriented Programming (OOP).

The project implements users, followers, tweets, replies, retweets, hashtags, timelines and trending topics while applying concepts such as inheritance, composition, abstract classes, special methods and unit testing.

## 🚀 Features

- User registration
- Follow other users
- Publish tweets
- Reply to publications
- Retweet posts
- Like publications
- Extract hashtags automatically
- Generate user timelines
- Calculate trending hashtags
- Load users and relationships from JSON
- Automated tests with pytest

## 🧱 Project Structure

```text
ChirpSocialNetwork/
├── datos/
│   └── usuarios.json
├── red_social/
│   ├── publicacion.py
│   ├── red.py
│   └── usuario.py
├── tests/
│   ├── conftest.py
│   ├── test_publicacion.py
│   ├── test_red.py
│   └── test_usuario.py
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## 🧠 OOP Concepts

The project applies several Object-Oriented Programming concepts:

- **Encapsulation** through classes such as `Usuario`, `Publicacion` and `RedSocial`
- **Inheritance** with different publication types
- **Abstract classes** using `ABC`
- **Composition** for replies and retweets
- **Special methods** such as `__str__`, `__eq__`, `__len__`, `__iter__`, `__contains__` and `__getitem__`
- **Properties**, class methods and static methods

## 🛠️ Technologies

- Python 3.12
- uv
- pytest
- Ruff

## ▶️ Running the Project

Clone the repository and enter the project directory:

```bash
git clone https://github.com/anto-rom/ChirpSocialNetwork.git
cd ChirpSocialNetwork
```

Install the project dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run main.py
```

## 🧪 Tests

Run the complete test suite with:

```bash
uv run pytest -v
```

The project includes tests for users, publications and the social network functionality.

Code quality can also be checked with Ruff:

```bash
uv run ruff check .
uv run ruff format --check .
```

## 📚 Purpose

This project was developed as a final Python exercise focused on applying Object-Oriented Programming concepts in a practical scenario.

The goal is to model the basic behaviour of a social network while maintaining a clear class structure and verifying its behaviour through automated tests.

## 👤 Author

**Antonio Romero**

GitHub: [@anto-rom](https://github.com/anto-rom)