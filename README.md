# Web Shop Test Automation

## Overview
This project automates the testing of user journeys/flows in a web application that includes browsing a product, searching a product, and checking out products.

## Project Structure
- `tests/`: Contains the test cases for different user journey flows.
- `pages/`: Implements the Page Object Model (POM) design pattern.
- `utils/`: Contains utility classes for WebDriver management and logging.
- `reports/`: Stores test execution reports.
- `Dockerfile`: Defines the Docker image setup for the project.

## Getting Started

### Prerequisites
- Docker
- Python 3.x

### Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sg_test_automation.git

2. Run Docker command:
   ```bash
   docker run -v <path>\sg_test_automation\reports:/app/reports sg_test_automation
