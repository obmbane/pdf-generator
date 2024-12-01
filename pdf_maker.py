from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)

def add_lines(start,finish,gap):

    y = start
    for i in range(start,finish,gap):
        pdf.line(10, y,200,y)
        y+=gap


df =pd.read_csv('topics_pdf_gen.csv')
#print (df)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=20)
    pdf.set_text_color(0,0,255)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=0)
    pdf.line(10,21,200,21)

    #add footer

    pdf.ln(265)
    pdf.set_font(family='Times',style='B',size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=8, txt=row['Topic'], align='R', ln=1, border=0)
    #Add pages with lines
    add_lines(31,290,10)
    
    for i in range (row['Pages']-1):
        pdf.add_page()
        #add footer
        pdf.ln(270)
        pdf.set_font(family='Times',style='B',size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=8, txt=row['Topic'], align='R', ln=1, border=0)
        #Add pages with lines
        add_lines(15,280,10)

pdf.output('output.pdf')