import os
import shutil
import logging
import winreg
from datetime import datetime

# Setup logging
logging.basicConfig(filename='smartlink.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class SmartLink:
    def __init__(self):
        self.backup_dir = "C:\\SmartLinkBackups"
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def recover_files(self, target_dir):
        logging.info(f"Attempting to recover files from {target_dir}")
        try:
            backup_path = os.path.join(self.backup_dir, os.path.basename(target_dir))
            if not os.path.exists(backup_path):
                raise FileNotFoundError("No backup found for the specified directory")
            for item in os.listdir(backup_path):
                s = os.path.join(backup_path, item)
                d = os.path.join(target_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            logging.info("File recovery successful")
        except Exception as e:
            logging.error(f"Error recovering files: {e}")
            raise

    def backup_files(self, source_dir):
        logging.info(f"Backing up files from {source_dir}")
        try:
            backup_path = os.path.join(self.backup_dir, os.path.basename(source_dir))
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
            shutil.copytree(source_dir, backup_path)
            logging.info("Backup successful")
        except Exception as e:
            logging.error(f"Error backing up files: {e}")
            raise

    def recover_system_settings(self):
        logging.info("Attempting to recover system settings")
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\SmartLinkBackup', 0, winreg.KEY_READ) as key:
                count = winreg.QueryInfoKey(key)[0]
                for i in range(count):
                    name, value, _ = winreg.EnumValue(key, i)
                    winreg.SetValueEx(winreg.HKEY_LOCAL_MACHINE, name, 0, winreg.REG_SZ, value)
            logging.info("System settings recovery successful")
        except Exception as e:
            logging.error(f"Error recovering system settings: {e}")
            raise

    def backup_system_settings(self):
        logging.info("Backing up system settings")
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE', 0, winreg.KEY_READ) as source_key:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\SmartLinkBackup') as backup_key:
                    count = winreg.QueryInfoKey(source_key)[0]
                    for i in range(count):
                        name, value, _ = winreg.EnumValue(source_key, i)
                        winreg.SetValueEx(backup_key, name, 0, winreg.REG_SZ, value)
            logging.info("System settings backup successful")
        except Exception as e:
            logging.error(f"Error backing up system settings: {e}")
            raise

    def schedule_backup(self, interval_hours):
        logging.info(f"Scheduling regular backups every {interval_hours} hours")
        # Scheduling logic can be implemented using Windows Task Scheduler
        # This can be done using `schtasks` from the command line
        # Example: os.system(f"schtasks /create /tn SmartLinkBackup /tr {__file__} /sc hourly /mo {interval_hours}")
        logging.warning("Backup scheduling functionality is not yet implemented")

if __name__ == "__main__":
    smartlink = SmartLink()
    # Example usage:
    # smartlink.backup_files("C:\\Users\\User\\Documents")
    # smartlink.recover_files("C:\\Users\\User\\Documents")
    # smartlink.backup_system_settings()
    # smartlink.recover_system_settings()
    # smartlink.schedule_backup(24)