# REST API Automated Testing Suite

Automated functional and regression test suite built with **Python**, **Requests**, and **PyTest** to validate RESTful API endpoints.

## Key Features
- **CRUD Operations Testing:** Automated test coverage for `GET`, `POST`, `PUT`, and `DELETE` endpoints.
- **Response Validation:** Verifies HTTP status codes (`200`, `201`, `404`), JSON schema fields, and payload accuracy.
- **Negative Testing:** Validates error handling for invalid resource IDs.
- **HTML Reporting:** Generates detailed test execution reports via `pytest-html`.

## How to Run
1. Install dependencies: `pip install requests pytest pytest-html`
2. Execute test suite: `pytest -v --html=report.html`
