# Digital Student Assistant

**Digital Student Assistant** is a Python-based web application designed to help students manage their academic projects efficiently. Built with Flask, it offers features like project tracking, applying for projects, scheduling, and more.

## Features

- **Project management**: Add, update, and delete academic projects.
- **Scheduling**: Organize tasks with due dates and priorities.
- **User-friendly interface**: Intuitive navigation for a smooth user experience.

## Project Structure

```
DigitalStudentAssistant/
├── app/             # Application modules and templates
├── migrations/      # Database migration files
├── tests.py         # Test cases
├── config.py        # Configuration settings
├── run.py           # Entry point to run the application
├── requirements.txt # Python dependencies
├── Procfile         # For deployment (e.g., Heroku)
└── app.db           # SQLite database file
```


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/eliray01/DigitalStudentAssistant.git
    cd DigitalStudentAssistant
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python run.py
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
