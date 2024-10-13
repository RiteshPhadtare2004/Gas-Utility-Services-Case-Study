# Gas Utility Case Study

This project is a simple Django application for managing gas utility services. It features an admin dashboard provided by Django and includes several routes for service submissions, tracking, and request management.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Running with Docker](#running-with-docker)
  - [Running without Docker](#running-without-docker)
- [Usage](#usage)
  - [How to Operate](#how-to-operate)
- [Routes](#routes)

## Features
- **Admin dashboard** for managing services.
- Three routes for handling service submissions, tracking, and customer request tracking.
  
## Technologies Used
- **Python 3.10**
- **Django**
- **Docker**

## Installation

### Running with Docker
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gas_utility_case_study.git
   cd gas_utility_case_study
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t gas_utility_case_study .
   ```

3. **Run the Docker container:**
   ```bash
   docker run -d -p 8000:8000 gas_utility_case_study
   ```

### Running without Docker
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gas_utility_case_study.git
   cd gas_utility_case_study
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate      # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for the admin portal:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

### How to Operate
1. **Access the Admin Dashboard:**
   - After creating a superuser, go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in with your superuser credentials.
   - From here, you can manage gas utility services.

2. **Submit a Service Request:**
   - Navigate to [http://127.0.0.1:8000/services/submit/](http://127.0.0.1:8000/services/submit/) to submit a new service request by filling out the form.

3. **Track a Service Request by ID:**
   - After submitting a service request, note down the ID (primary key) of the request.
   - You can track the request by going to the URL [http://127.0.0.1:8000/track/<pk>](http://127.0.0.1:8000/track/<pk>), replacing `<pk>` with the actual ID of your request.

4. **Track a Service Request by Email and Date:**
   - A new feature has been added to allow customers to track their service requests using their email and the date the request was made.
   - Navigate to [http://127.0.0.1:8000/services/track_request/](http://127.0.0.1:8000/services/track_request/) and fill in your registered email and the request date to track your request.
   - This route enables you to track your request without needing the specific request ID, offering more flexibility for customers.

## Routes
1. **Admin Dashboard:**  
   Access the admin dashboard at `/admin/`.

2. **Service Submission:**  
   Submit a service request at `/services/submit/`.

3. **Track Service Request by ID:**  
   Track a service request by ID at `/track/<pk>/`, where `<pk>` is the primary key of the service request.

4. **Track Service Request by Email and Date:**  
   Track a service request by providing your email and request date at `/services/track_request/`.
