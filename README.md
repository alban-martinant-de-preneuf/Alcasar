# Alcasar LDAP users to group

This project is a script that interacts with LDAP and MySQL to automate the process of adding users to an LDAP group. The script searches for posixAccount objects, retrieves their uids, and then adds them to the specified LDAP group in the MySQL database used by Alcasar.

## Project Overview

The primary objective of the Alcasar project is to simplify the management of LDAP groups by automating the process of adding users. The script connects to the LDAP server, retrieves user uids, and then connects to the MySQL database to execute SQL queries for adding users to the specified group.

## Features

- Automates the process of adding users to an LDAP group in Alcasar.
- Retrieves user uids from posixAccount objects in the LDAP directory.
- Utilizes MySQL queries to add users to the appropriate LDAP group in the database.

## Usage

1. Clone this repository to your local machine.
2. Make sure you have the required dependencies, such as the `ldap3` and `mysql-connector-python` packages.
3. Modify the script as needed to specify the LDAP server address, LDAP search base, and MySQL configuration.
4. Ensure you have the appropriate privileges and access to the LDAP server and MySQL database.
5. Run the script using a Python interpreter: `python LDAPusersToGroup.py`.

## Dependencies

- `ldap3`: Python library for interacting with LDAP directories.
- `mysql-connector-python`: Python library for interacting with MySQL databases.

## Note

- Make sure to configure the script with the correct LDAP server information and MySQL credentials before running it.
- The script is designed to add users to the specified LDAP group in the Alcasar MySQL database.

## Contributions

Contributions and suggestions are welcome! If you have ideas to enhance this script, improve its functionality, or handle edge cases, feel free to create an issue or a pull request.

## Disclaimer

Please note that this project is intended for specific use cases and may require customization to fit different environments. It's recommended to review and test the script thoroughly before using it in a production environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
