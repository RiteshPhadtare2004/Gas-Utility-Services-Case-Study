# Gas Utility Case Study

This project is a simple Django application for managing gas utility services. It features an admin dashboard provided by Django and includes two primary routes.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [License](#license)

## Features
- Admin dashboard for managing services
- Two routes for handling service submissions

## Technologies Used
- Python 3.10
- Django
- Docker

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gas_utility_case_study.git
   cd gas_utility_case_study

2. **Build the Docker image:**

    ```bash
    docker build -t gas_utility_case_study .

2. **Run the Docker container:**

    ```bash
    docker run -d -p 8000:8000 gas_utility_case_study
