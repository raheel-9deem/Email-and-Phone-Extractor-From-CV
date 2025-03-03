Bulk Resume Parser

 📌 Overview

This Python-based tool allows you to extract **Name, Email, and Phone Number** from multiple resumes (PDF, PNG, JPG). Simply provide a folder containing resumes, and the tool will generate an Excel file with the extracted details.

⚡ Features

- 🔍 **Bulk Resume Processing** – Extracts data from multiple resumes at once.
- 📄 **Supports PDF & Image Files** – Works with `.pdf`, `.png`, `.jpg`, and `.jpeg` formats.
- 📊 **Saves Output in Excel** – Generates `bulk_resumes_details.xlsx` with extracted details.
- 🖥️ **User-Friendly** – Simple GUI for folder selection.

🛠️ Requirements

Make sure you have the following installed:

- Python 3.x
- Required Python libraries:
  ```sh
  pip install opencv-python pytesseract pdfplumber pandas tk
  ```
- **Tesseract OCR** (for image text extraction) – [Download Here](https://github.com/UB-Mannheim/tesseract/wiki)

🚀 How to Use

1. **Clone the Repository**
2. **Run the Script**
   ```sh
   python app.py
   ```
3. Select Folder
   - A file dialog will open, allowing you to select a folder containing resumes.
4. Check Output
   - The tool will extract data and save it in `bulk_resumes_details.xlsx`.

📝 Output Format (Excel File)

| Filename    | Name       | Email                                                | Phone         |
| ----------- | ---------- | ---------------------------------------------------- | ------------- |
| resume1.pdf | John Doe   | [john.doe@email.com](mailto\:john.doe@email.com)     | +123-456-7890 |
| resume2.png | Jane Smith | [jane.smith@email.com](mailto\:jane.smith@email.com) | +987-654-3210 |

🤝 Contributing

Feel free to **fork this repository** and submit pull requests for improvements!

📜 License

This project is licensed under the MIT License. Feel free to modify and distribute it.

🔹 Developed by **Raheel Nadeem** 🚀

