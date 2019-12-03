from PyPDF2 import PdfFileMerger

def merge_pdf():
	pdfs = ['PAGE 1.pdf', 'PAGE 2.pdf', 'PAGE 3.pdf', 'PAGE 4.pdf', 'PAGE 5.pdf']
	merger = PdfFileMerger()
	for pdf in pdfs:
	    merger.append(pdf)
	merger.write("Result.pdf")
	merger.close()

if __name__ == '__main__':
	merge_pdf()