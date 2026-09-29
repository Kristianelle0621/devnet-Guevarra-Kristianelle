"""
Module 2 — Activity: File Sorting with os and shutil
Student: Guevarra, Kristianelle P.
Date: 09/29/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built an simple automated Python code that can scan a specified folder and organize the loose files into a category subfolders based on their file extensions.

============================================
KEY VOCABULARY
============================================
- os module: it's a built in pyhton library used to check files and more
- shutil module: a built in pyhton library used to move, copy, or delete files
- file path: the exact address of the file
- directory: another name for a computer folder 
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""
import os
import shutil

FILE_GROUPS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp"]
}

def organize_folder(folder_path="."):

    base_path = os.path.abspath(folder_path)

    if not os.path.exists(base_path) or not os.path.isdir(base_path):
        print(f"Error: Directory '{base_path}' does not exist.")
        return

    total_organized = 0

    for file_item in os.listdir(base_path):
        source_path = os.path.join(base_path, file_item)

        if os.path.isdir(source_path):
            continue

        base_name, file_ext = os.path.splitext(file_item)
        file_ext = file_ext.lower()

        if not file_ext:
            continue

        assigned_folder = "Others"
        for group_name, valid_extensions in FILE_GROUPS.items():
            if file_ext in valid_extensions:
                assigned_folder = group_name
                break

        output_directory = os.path.join(base_path, assigned_folder)
        os.makedirs(output_directory, exist_ok=True)

        final_destination = os.path.join(output_directory, file_item)

        if os.path.exists(final_destination):
            final_destination = os.path.join(output_directory, f"{base_name}_copy{file_ext}")

        shutil.move(source_path, final_destination)
        print(f"Moved: '{file_item}' -> '{assigned_folder}/'")
        total_organized += 1

    print(f"\nSorting complete! Successfully organized {total_organized} file(s).")

if __name__ == "__main__":
    user_path = input("Enter folder path to organize (press Enter for current directory): ").strip()
    organize_folder(user_path if user_path else ".")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
the uppercase and lowercase extension because i forgot to put a ignoring case so it can stil read the file even it's all caps or low caps.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
