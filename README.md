<<<<<<< HEAD
# Dockerized-Notes-App
=======
# half vibe-coded project using gemini cli
# Gooners-Notes

A simple, containerized note-taking application built with **Flask** and **Redis**. This project demonstrates how to orchestrate a Python web application with a NoSQL database using Docker Compose.

## 🚀 Features

*   **Add Notes:** Quickly save text-based notes.
*   **Delete Notes:** Remove notes when you're done.
*   **Persistent Storage:** Uses Redis volumes to ensure data survives container restarts.
*   **Dockerized:** Fully containerized setup for consistent development and deployment.

## 🛠️ Tech Stack

*   **Frontend/Backend:** Python (Flask)
*   **Database:** Redis (Alpine)
*   **Infrastructure:** Docker & Docker Compose

## 🏁 Getting Started

### Prerequisites

*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Run

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd neon_notes
    ```

2.  **Start the application:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the App:**
    Open your browser and navigate to:
    [http://localhost:5000](http://localhost:5000)

## 📂 Project Structure

*   `app.py`: Main Flask application logic.
*   `Dockerfile`: Configuration for building the Python web image.
*   `docker-compose.yaml`: Orchestration for Web and Redis services.
*   `redis_data/`: Local directory mapped to the container for data persistence.
>>>>>>> 6aca211 (added readme)
