

---

````markdown
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

🎉 *Happy book managing!*

```



**My name is Emre Hacıhassan, ı developed this project in collaboration with Instructor Sercan as part of the Python 1 course at Enstitü İstanbul İSMEK.**
