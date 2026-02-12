# Oytra-Assess

A Python-based data parsing assessment project for Oytra.

## Overview

This project demonstrates data parsing capabilities using modern Python development practices. It includes a structured approach to handling member signup files and processing them through a dedicated parsing module.

## Project Structure

```
Oytra-Assess/
├── data/
│   └── raw/              # Raw data files for parsing
├── src/
│   └── oytra_assess/     # Main package module
├── pyproject.toml        # Project configuration and dependencies
├── uv.lock              # Lock file for reproducible builds
├── .python-version      # Python version specification
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Prerequisites

- Python 3.13
- uv

## Installation

### Using uv (Recommended)

1. Install uv if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/monkeplication/Oytra-Assess.git
   cd Oytra-Assess
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```
## Development

### Setting Up Development Environment

```bash
# Install development dependencies
uv sync --all-extras
```

### Project Configuration

The project uses `pyproject.toml` for configuration, following modern Python packaging standards. All project metadata, dependencies, and tool configurations are centralized in this file.

## Data

Signup.xls should be placed in the `data/raw/` directory. The parsing module in `src/oytra_assess/` is designed to process these files.

## Dependencies

Dependencies are managed through `pyproject.toml` and locked in `uv.lock` for reproducible installations across environments.
