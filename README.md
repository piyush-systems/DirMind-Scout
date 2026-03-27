# 🧠 DirMind Scout

DirMind Scout is a Python-based system analysis tool that scans your directories and provides intelligent insights about your files.

It helps you quickly identify:

* 🗑 Empty folders
* 📦 Large files
* ⏳ Old / unused files

---

## 🚀 Features

### 📂 Empty Folder Detection

Finds directories that contain no files or subfolders.

### 📊 Large File Analyzer

Identifies the largest files in your system with readable size formatting.

### ⏳ Old File Detector

Detects files that haven’t been modified for a given number of days.

### 🔍 Interactive Selection

Select files/folders by number to view full paths.

---

## 🧠 Why DirMind Scout?

Instead of manually browsing through your system, DirMind Scout gives you a **clear, structured overview** of:

* Unused directories
* Storage-heavy files
* Forgotten files

---

## ▶️ Usage

```bash
python DirMind_Scout.py "path_to_directory"
```

Example:

```bash
python DirMind_Scout.py "C:\Users\User\Desktop"
```

---

## 📸 Sample Output

```
========== DirMind Summary ==========
📁 Empty Folders : 3
📄 Total Files   : 128
⚠️ Unused directories detected

========== DirMind Menu ==========
1. View Empty Folders
2. View Large Files
3. View Old Files
4. Exit

👉 Enter [1/2/3/4]: 2

========== Top Large Files ==========
 1. videos/project_demo.mp4              512.34 MB
 2. backups/old_backup.zip              243.10 MB
 3. datasets/data.csv                   120.45 MB
 4. downloads/setup.exe                 95.22 MB
 5. images/high_res.png                 72.89 MB

🔍 Enter numbers to view full paths: 1,3

========== Selected Full Paths ==========
- C:\Users\User\Desktop\videos\project_demo.mp4
- C:\Users\User\Desktop\datasets\data.csv
```

---

## 🧩 Future Scope

DirMind Scout is part of a larger system:

> 🔥 DirMind System (Analyzer + Cleaner + Automation)

Planned improvements:

* File cleanup automation
* Advanced duplicate detection
* Smart suggestions engine

---

## 👨‍💻 Author

Built by Piyush
Focused on building intelligent systems and tools.

---

## ⭐ Feedback

Suggestions and improvements are always welcome!
