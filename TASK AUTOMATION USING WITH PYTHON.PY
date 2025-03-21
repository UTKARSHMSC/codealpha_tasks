import os
import shutil
import time
import schedule

# Function to organize files by type
def organize_files(source_folder):
    if not os.path.exists(source_folder):
        print("Source folder does not exist!")
        return
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            folder_path = os.path.join(source_folder, file_extension)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved {filename} to {folder_path}")

# Function to schedule daily file organization
def schedule_task():
    source_directory = "C:/Users/YourUsername/Desktop/TestFolder"  # Change as needed
    schedule.every().day.at("10:00").do(organize_files, source_directory)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    print("Starting automated file organization...")
    schedule_task()
