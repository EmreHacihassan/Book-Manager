# 📚 Book Database Project

A desktop application built with **Python 3.10** and **PyQt6**, allowing users to manage a personal book collection via a clean graphical interface and a local **SQLite** database. Designed for educational and lightweight use cases.

---

## ✨ Features

- Add new books with detailed metadata
- List all books from the database
- View and edit book information:
  - Title
  - Publication Year
  - Page Count
  - Language
  - Publisher
  - Description
- Update or delete selected books
- Modern GUI using PyQt6
- Uses SQLite (built-in; no external database setup required)

---

## 📦 Requirements

- Python 3.10+
- All dependencies are listed in `requirements.txt`

### Install Dependencies

```bash
pip install -r requirements.txt
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Book_Database_Project.git
cd Book_Database_Project
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate
```

**Windows CMD:**

```cmd
venv\Scripts\activate.bat
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Optional: Regenerate UI File

If you modify the `kitap.ui` file via Qt Designer, regenerate `kitap.py`:

```bash
python -m PyQt6.uic.pyuic -x kitap.ui -o kitap.py
```

### Launch the App

```bash
python main.py
```

---

## 🖼️ GUI Overview

| Field                | Description              |
| -------------------- | ------------------------ |
| **Book No**          | Auto-incremented book ID |
| **Book Name**        | Title of the book        |
| **Publication Year** | Year of publication      |
| **Page Count**       | Total pages in the book  |
| **Language**         | Selectable dropdown menu |
| **Publisher**        | Selectable dropdown menu |
| **Description**      | Free-text area           |

### Action Buttons

* **EKLE (Add):** Insert a new book
* **LİSTELE (List):** Populate the dropdown list with all books
* **Kitap Getir (Get Book):** Load details of selected book
* **Güncelle (Update):** Update book information
* **SİL (Delete):** Remove selected book from the database
* **ÇIKIŞ (Exit):** Close the application

---

## 🔁 Common Workflow

1. **Add a Book:** Fill in the form → Click **EKLE**
2. **List All Books:** Click **LİSTELE**
3. **View Book Details:** Select a book → Click **Kitap Getir**
4. **Edit & Update:** Change fields → Click **Güncelle**
5. **Delete Book:** Select → Click **SİL**


```

---

## 🛠️ Troubleshooting

| Issue                              | Solution                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| **PyQt6 not found**                | Make sure `venv` is activated, and run `pip install -r requirements.txt`.              |
| **UI changes not appearing**       | Re-run the UI generation command: `python -m PyQt6.uic.pyuic -x kitap.ui -o kitap.py`. |
| **Database issues**                | Delete `arsivci.db` to reset the database (⚠️ all data will be lost).                  |
| **PowerShell script policy error** | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`            |

---

## 📌 Notes

* Data is stored **locally** in `arsivci.db`
* Designed for small-scale or personal use
* GUI can be visually modified via **Qt Designer**
* No internet or server connection is needed
* Created during Python 1 training with **Instructor Sercan**

---

## 📄 License

This project is intended for educational and personal use.
Feel free to modify or expand it under your own licensing terms.

---


## 🧪 How to Run the Application — Step by Step

Follow these steps to set up and run the project on your local machine:

### ✅ 1. Download or Clone the Project

If you have Git installed:

```bash
git clone https://github.com/yourusername/Book_Database_Project.git
cd Book_Database_Project
```

Or simply download the ZIP file from GitHub and extract it.

---

### ✅ 2. Create a Virtual Environment (Recommended)

Creating a virtual environment helps you manage project dependencies separately from your system Python.

```bash
python -m venv venv
```

Then activate it:

* **Windows PowerShell:**

```powershell
.\venv\Scripts\Activate
```

* **Windows CMD:**

```cmd
venv\Scripts\activate.bat
```

> 💡 You should see `(venv)` at the beginning of your terminal line if the virtual environment is active.

---

### ✅ 3. Install the Required Packages

Use the provided `requirements.txt` file to install the needed Python packages:

```bash
pip install -r requirements.txt
```

---

### ✅ 4. (Optional) Update the UI File if You Made Changes

If you edited `kitap.ui` using Qt Designer, convert it back to a Python file:

```bash
python -m PyQt6.uic.pyuic -x kitap.ui -o kitap.py
```

---

### ✅ 5. Run the Application

Start the application using the main script:

```bash
python main.py
```

This will open the main window of the Book Manager application.

---

### 🧭 Example Usage Flow

1. **Add a Book:** Fill in the form and click `EKLE`.
2. **List Books:** Click `LİSTELE` to view all saved books.
3. **View Details:** Select a book and click `Kitap Getir`.
4. **Edit Info:** Make changes and click `Güncelle`.
5. **Delete a Book:** Select and click `SİL`.
6. **Exit the App:** Click `ÇIKIŞ` to close the program.

---

🎉 *Happy book managing!*

```




**My name is Emre Hacıhassan, ı developed this project in collaboration with Instructor Sercan as part of the Python 1 course at Enstitü İstanbul İSMEK.**
