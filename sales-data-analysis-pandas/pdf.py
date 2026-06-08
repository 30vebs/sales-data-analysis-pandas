import pdfplumber
import pandas as pd
import os

pdf_folder = r"C:\Users\YV264RF\OneDrive - EY\Desktop\Vaibhav personal"
output_file = "output.xlsx"

all_data = []

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        print(f"📄 Processing file: {file}")  # ✅ Add this

        pdf_path = os.path.join(pdf_folder, file)

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                print(f"   ➤ Page {i+1}")  # ✅ Add this

                table = page.extract_table()

                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    df["Source_File"] = file
                    all_data.append(df)

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_excel(output_file, index=False)
    print("✅ Done! Excel file created:", output_file)
else:
    print("⚠️ No tables found")