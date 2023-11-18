# # Import Module
# import tabula

# # Read PDF File
# # this contain a list
# df = tabula.read_pdf('C:/Users/Neebal/Documents/stmt_76130100024205_1672206732158_221228_112219.pdf', pages = 1)[4]

# # Convert into Excel File
# df.to_excel('D:/python/bank statement poc/Book1.xlsx')


import io
from tabula import read_pdf
import PyPDF2


# file='C:/Users/Neebal/Documents/stmt_76130100024205_1672206732158_221228_112219.pdf'
file='BL - TARMAL.PDF'
df=[]
file = open(file, 'rb')
readpdf = PyPDF2.PdfReader(file)
totalpages = len(readpdf.pages)
print(totalpages)

for i in range (1,totalpages):
    #reads table from pdf file
    # df=read_pdf(file,pages=i)
    df.append(read_pdf(file,pages=i)) #address of pdf file
    # file1 = open('myfile.txt', 'w')
    print("PAGE NUMBER "+str(i))
    for row in df:
        print(row)
        for data in row:
                data.to_excel('Book1.xlsx', sheet_name='Sheet1',header=True)
    
# print(df[0])
# # df.to_excel('Book1.xlsx', sheet_name='Sheet1')
