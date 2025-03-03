import os
import cv2
import pytesseract
import pdfplumber
import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog

# Set Tesseract Path (Change this if needed)
pytesseract.pytesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from an image
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text

# Function to extract name, email, and phone
def extract_details(text):
    name_match = re.search(r"([A-Z][a-z]+(?: [A-Z][a-z]+)*)", text)
    name = name_match.group(1).strip() if name_match else "Not Found"
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"\+?\d{1,3}[\s-]?(\d{3})[\s-]?(\d{3})[\s-]?(\d{4})", text)
    phone = ["-".join(match) for match in phone]
    
    return {
        "Name": name,
        "Email": email[0] if email else "Not Found",
        "Phone": phone[0] if phone else "Not Found"
    }

# Function to process all resumes in a folder
def process_resumes(folder_path):
    data = []
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.endswith((".png", ".jpg", ".jpeg")):
            text = extract_text_from_image(file_path)
        else:
            continue  # Skip unsupported files
        
        details = extract_details(text)
        details["Filename"] = file
        data.append(details)
    
    df = pd.DataFrame(data)
    df.to_excel("bulk_resumes_details.xlsx", index=False)
    print("✅ Bulk Resume Parsing Completed! Check 'bulk_resumes_details.xlsx'")

# Folder selection dialog
def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select Folder Containing Resumes")
    if folder_path:
        process_resumes(folder_path)
    else:
        print("❌ No folder selected.")

# Run the tool
print("📂 Please select a folder containing resumes...")
select_folder()
