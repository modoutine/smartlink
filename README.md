# SmartLink

SmartLink is a powerful utility designed to assist users in recovering lost files and system settings on Windows devices. It offers easy-to-use tools for backing up and restoring critical data, ensuring that your important information is always secure.

## Features

- **File Recovery**: Restore files from specified directories that have been previously backed up.
- **File Backup**: Create backups of important directories to a secure location.
- **System Settings Backup and Recovery**: Save and restore critical system settings from the Windows registry.
- **Scheduled Backups**: Plan regular backups at specified intervals.

## Installation

To use SmartLink, ensure that you have Python installed on your Windows device. You can download Python from the [official website](https://www.python.org/downloads/).

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smartlink.git
   ```

2. Navigate to the directory:
   ```bash
   cd smartlink
   ```

3. Run the script:
   ```bash
   python smartlink.py
   ```

## Usage

1. **Backup Files**: To backup files from a directory, use the `backup_files` method.
   ```python
   smartlink.backup_files("C:\\Path\\To\\Your\\Directory")
   ```

2. **Recover Files**: To recover files to a directory, use the `recover_files` method.
   ```python
   smartlink.recover_files("C:\\Path\\To\\Your\\Directory")
   ```

3. **Backup System Settings**: To backup system settings, use the `backup_system_settings` method.
   ```python
   smartlink.backup_system_settings()
   ```

4. **Recover System Settings**: To recover system settings, use the `recover_system_settings` method.
   ```python
   smartlink.recover_system_settings()
   ```

5. **Schedule Backup**: Although the scheduling feature is not fully implemented, you can use Windows Task Scheduler to automate backups.
   ```python
   smartlink.schedule_backup(24)
   ```

## Logs

All actions performed by SmartLink are logged in `smartlink.log` for troubleshooting and record-keeping.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.