import PyPDF2
import os


def mergepdf():
    merger = PyPDF2.PdfMerger()
    # Get a list of all PDF files in the directory
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
    # Write the merged PDF to the output file
    merger.write("combined.pdf")


def splitpdf():
    input_pdf = ""
    # Get the only one PDF file in the directory
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            input_pdf = file
            break
    # This is input control
    if len(input_pdf) == 0:
        print('No pdf file found!')
        return None

    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Iterate through each page and save it as a separate PDF
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            output_pdf = f"page_{page_num + 1}.pdf"
            with open(output_pdf, "wb") as output_file:
                pdf_writer.write(output_file)

            print(f"Page {page_num + 1} saved as {output_pdf}")


menu = int(input("Please input 1 for merge PDF files, 2 for split PDF files: "))
if menu == 1:
    mergepdf()
elif menu == 2:
    splitpdf()
else:
    print("Invalid input!")
