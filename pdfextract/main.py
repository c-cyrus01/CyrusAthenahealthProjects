import pdfkit

# Read the PDF file

pdf_file = open(
    "/Users/christophercyrus/PycharmProjects/pdfextract/PN-234937_12616-Ballantyne Family Medicine PC-Outbound Automated Report Delivery-CCP-25386309-06-2023-19-15-57.pdf",
    "rb",
)

# Convert the PDF to HTML

html_file = pdfkit.from_file(pdf_file, "my_html_file.html")

# Close the PDF file

pdf_file.close()
