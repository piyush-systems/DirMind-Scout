import os
import sys
import time


# ------------------ DATA LAYER ------------------

def find_empty_folders(path):
    return [root for root, dirs, files in os.walk(path) if not dirs and not files]


def scan_files(path):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                files_list.append((full_path, size))
            except:
                continue
    return files_list


def get_top_large_files(files_list, n=5):
    return sorted(files_list, key=lambda x: x[1], reverse=True)[:n]


def get_old_files(path, days_threshold):
    old_files = []
    current_time = time.time()

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                modified_time = os.path.getmtime(full_path)
                days_old = int((current_time - modified_time) / (60 * 60 * 24))

                if days_old >= days_threshold:
                    old_files.append((full_path, days_old))
            except:
                continue

    return sorted(old_files, key=lambda x: x[1], reverse=True)


# ------------------ UTILITY ------------------

def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def header(title):
    print(f"\n{'='*10} {title} {'='*10}")


# ------------------ DISPLAY ------------------

def display_folders(emp_folders, base_path):
    header("Empty Folders")

    if not emp_folders:
        print("✅ No empty folders found")
        return

    for i, folder in enumerate(emp_folders, 1):
        rel = os.path.relpath(folder, base_path)
        print(f"{i:>2}. {rel}")

    print(f"\n📊 Total: {len(emp_folders)}")


def display_large_files(largefiles_list, base_path):
    header("Top Large Files")

    for i, (file, size) in enumerate(largefiles_list, 1):
        rel = os.path.relpath(file, base_path)
        print(f"{i:>2}. {rel:<40} {format_size(size):>10}")


def display_old_files(old_files, base_path, limit=10):
    header("Old Files")

    if not old_files:
        print("✅ No old files found")
        return

    for i, (file, days) in enumerate(old_files[:limit], 1):
        rel = os.path.relpath(file, base_path)
        print(f"{i:>2}. {rel:<40} {days} days old")

    if len(old_files) > limit:
        print(f"\n...and {len(old_files) - limit} more files")


# ------------------ INTERACTION ------------------

def handle_selection(items):
    choice = input("\n🔍 Enter numbers to view full paths (comma separated) or press Enter to skip: ").strip()

    if not choice:
        return

    try:
        indexes = [int(x.strip()) - 1 for x in choice.split(",")]

        header("Selected Full Paths")
        for i in indexes:
            if 0 <= i < len(items):
                print(f"- {items[i]}")
            else:
                print(f"❌ Invalid index: {i+1}")

    except ValueError:
        print("❌ Invalid input format")


# ------------------ HANDLERS ------------------

def handle_empty_folders(emp_folders, path):
    display_folders(emp_folders, path)
    handle_selection(emp_folders)


def handle_large_files(files_list, path):
    if not files_list:
        print("\n⚠️ No files found")
        return

    large_files = get_top_large_files(files_list)
    display_large_files(large_files, path)

    file_paths = [file for file, _ in large_files]
    handle_selection(file_paths)


def handle_old_files(path):
    try:
        days = int(input("⏳ Enter days threshold (e.g. 180): ").strip())
    except ValueError:
        print("❌ Invalid number")
        return

    old_files = get_old_files(path, days)
    display_old_files(old_files, path)

    file_paths = [file for file, _ in old_files]
    handle_selection(file_paths)


# ------------------ MAIN ------------------

def main():
    if len(sys.argv) < 2:
        path = input("Enter path: ")
    else:
        path = sys.argv[1]

    if not os.path.exists(path):
        print("❌ Path does not exist")
        return

    if not os.path.isdir(path):
        print("❌ Path is not a directory")
        return

    emp_folders = find_empty_folders(path)
    files_list = scan_files(path)

    # 🔥 Clean Summary
    header("DirMind Summary")
    print(f"📁 Empty Folders : {len(emp_folders)}")
    print(f"📄 Total Files   : {len(files_list)}")

    if emp_folders:
        print("⚠️ Unused directories detected")
    if len(files_list) > 100:
        print("⚠️ Large number of files — consider cleanup")

    # 🔥 Menu Loop
    while True:
        header("DirMind Menu")
        print("1. View Empty Folders")
        print("2. View Large Files")
        print("3. View Old Files")
        print("4. Exit")

        choice = input("👉 Enter [1/2/3/4]: ").strip()

        if choice == "1":
            handle_empty_folders(emp_folders, path)

        elif choice == "2":
            handle_large_files(files_list, path)

        elif choice == "3":
            handle_old_files(path)

        elif choice == "4":
            print("\n👋 Exiting DirMind...")
            break

        else:
            print("❌ Invalid input")


if __name__ == "__main__":
    main()