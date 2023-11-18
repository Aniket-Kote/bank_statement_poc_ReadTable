import io
from tabula import read_pdf
import PyPDF2
import openpyxl

# file='C:/Users/Neebal/Documents/stmt_76130100024205_1672206732158_221228_112219.pdf'
file='sbi.pdf'
df=[]
file = open(file, 'rb')
readpdf = PyPDF2.PdfReader(file)
totalpages = len(readpdf.pages)
print(totalpages)


for i in range(1,totalpages):
    df.append(read_pdf(file,pages=i)) #address of pdf file



wb = openpyxl.Workbook()
ws = wb.active

for i in df:
    ws.append(i)
    
wb.save('Book1.xlsx')