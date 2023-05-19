# attendance-bot

The Student Attendance Telegram Bot is a Python-based bot that allows educational institutions to track and manage student attendance through Telegram. This bot provides an easy-to-use interface for administrators to add students, record attendance, generate attendance reports, and more.

## Table of Contents

- [attendance-bot](#attendance-bot)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Configuration](#configuration)
  - [License](#license)

## Installation

To install and set up the Student Attendance Telegram Bot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip` or `pipenv`.
3. Set up the necessary configuration files and environment variables.
4. Start the bot using the appropriate command.

For detailed installation instructions, please refer to the [Installation Guide](docs/installation.md).

## Usage

Once the bot is installed and configured, you can start using it to manage student attendance. Here are some of the key features:

- **Adding Students**: Administrators can add students to the system by providing their details such as name, group, and Telegram ID.
- **Recording Attendance**: The bot allows administrators to record student attendance by marking them as present or absent for specific dates.
- **Generating Reports**: Attendance reports can be generated in Excel format, organized by student groups, with columns indicating attendance status for each date.
- **Admin Privileges**: Certain commands and features are accessible only to administrators, ensuring proper access control.

For detailed instructions on how to use the bot, please refer to the [User Guide](docs/usage.md).

## Project Structure

The project follows a modular structure for easy maintenance and extensibility. The main components of the project are:

- `bot.py`: Entry point of the bot application.
- `handlers/`: Contains the message and callback handlers for different commands and interactions.
- `filters/`: Custom filters for message and callback filtering.
- `keyboards/`: Keyboard layouts for interactive user interfaces.
- `states/`: States and state handlers for managing user conversation flows.
- `lexicon/`: Language files for localization and text resources.
- `database/`: Database models, migrations, and database-related operations.
- `utils/`: Utility functions and helper modules.
- `config/`: Configuration files for the bot.
- `.env`: Environment variables for sensitive configuration.

For a detailed explanation of the project structure, refer to the [Project Structure Guide](docs/project-structure.md).

## Configuration

The bot can be configured using the provided configuration files and environment variables. The following parameters can be customized:

- `TOKEN`: Telegram Bot API token.
- `DB_URI`: Database connection URI.
- Other bot-specific settings, such as command prefixes, admin IDs, etc.

## License

This project is licensed under the [MIT License](LICENSE).