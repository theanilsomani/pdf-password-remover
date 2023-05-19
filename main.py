from PyPDF2 import PdfReader, PdfWriter


# change the file name in PdfReader("")
reader = PdfReader("P_936_159174044.pdf")
writer = PdfWriter()

# write the password at .decrypt("")
if reader.is_encrypted:
    reader.decrypt("1591740442604")

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Save the new PDF to a file
with open("decrypted-pdf.pdf", "wb") as f:
    writer.write(f)