import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def sort_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist!")
            return

        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Get file extension
            extension = file.split('.')[-1]

            # Create folder for extension
            extension_folder = os.path.join(folder_path, extension.upper())

            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Move file
            shutil.move(file_path, os.path.join(extension_folder, file))

            logging.info(f"Moved: {file} -> {extension_folder}")

        print("Files sorted successfully!")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("An error occurred:", e)


def rename_files(folder_path, prefix):
    try:
        files = os.listdir(folder_path)

        count = 1

        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                extension = file.split('.')[-1]
                new_name = f"{prefix}_{count}.{extension}"

                new_path = os.path.join(folder_path, new_name)

                os.rename(file_path, new_path)

                logging.info(f"Renamed: {file} -> {new_name}")

                count += 1

        print("Files renamed successfully!")

    except Exception as e:
        logging.error(f"Rename Error: {e}")
        print("Error:", e)


def delete_temp_files(folder_path):
    try:
        files = os.listdir(folder_path)

        for file in files:
            if file.endswith('.tmp'):
                file_path = os.path.join(folder_path, file)

                os.remove(file_path)

                logging.info(f"Deleted temp file: {file}")

        print("Temporary files cleaned!")

    except Exception as e:
        logging.error(f"Cleaning Error: {e}")
        print("Error:", e)


# Main Program
print("==== File Automation Script ====")

folder = input("Enter folder path: ")

print("""
1. Sort Files
2. Rename Files
3. Delete Temp Files
""")

choice = input("Enter your choice: ")

if choice == '1':
    print("Sortinf files")
    sort_files(folder)
    print("Files Sorted")

elif choice == '2':
    prefix = input("Enter prefix for files: ")
    rename_files(folder, prefix)

elif choice == '3':
    print("Deleting files")
    delete_temp_files(folder)
    print("Files deleted sucessfully")

else:
    print("Invalid choice!")