from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P',unit='mm',format='A4')

df =pd.read_csv('topics_pdf_gen.csv')
print (df)

for index, row in df.iterrows():
    num_pages = int(row['Pages'])

    for i in range (num_pages):
        pdf.add_page()
        pdf.set_font(family='Times',style='B',size=20)
        pdf.cell(w=10, h=12, txt=row['Topic'], align='L', ln=1, border=0)

pdf.output('output.pdf')