# 🧹 Oytra-Assess  
**Python Data Parsing Assessment Project**

A structured Python project demonstrating data parsing, cleaning, and processing using modern development practices.

---

## 📌 Overview

This project showcases:

- Parsing and cleaning structured signup data  
- Organizing code using a proper Python package structure  
- Managing dependencies with `uv`  
- Following modern Python packaging standards (`pyproject.toml`)  
- Producing reproducible builds using a lock file  

The goal is to transform messy member signup data into a clean, structured output ready for CRM ingestion.

---

## 🗂 Project Structure

```
Oytra-Assess/
├── data/
│   └── raw/                # Raw signup files (input)
│
├── src/
│   └── oytra_assess/       # Core parsing and processing logic
│
├── pyproject.toml          # Project metadata & dependencies
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version specification
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## ⚙️ Prerequisites

- Python 3.13  
- uv (fast Python package manager)

---

## 🚀 Installation

### 1. Install `uv` (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository

```bash
git clone https://github.com/monkeplication/Oytra-Assess.git
cd Oytra-Assess
```

### 3. Install Dependencies

```bash
uv sync
```

This installs all dependencies exactly as defined in `uv.lock` for reproducibility.

---

## 🛠 Development Setup

To install development dependencies (if defined in extras):

```bash
uv sync --all-extras
```

---

## 📄 Project Configuration

The project follows modern Python packaging standards using:

- `pyproject.toml` — Centralized configuration for:
  - Project metadata
  - Dependencies
  - Tooling configuration
- `uv.lock` — Ensures consistent environments across machines

This keeps the project clean, reproducible, and production-ready.

---

## 📊 Data Instructions

Place the input file:

```
Signup.xls
```

inside:

```
data/raw/
```

The parsing module inside:

```
src/oytra_assess/
```

will process the file and generate the cleaned output.

---

## 🔒 Dependency Management

- Dependencies are defined in `pyproject.toml`
- Exact versions are locked in `uv.lock`
- Ensures consistent builds across systems and CI environments

---

## 📜 License

This repository is part of a technical assessment for Oytra.
