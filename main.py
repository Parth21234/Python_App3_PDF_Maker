from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format='A4')

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100, 100, 100) # Grey, values for r,g,b.
    # For red, 254,0,0.
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(10, 21, 200,21)
    # The arguments of the line method will be x1,y1,x2,y2.

# border = 1 is for the box around the texts.
# ln is actually a break line.
# height 'h' has to be set as same as size of the font/text.

pdf.output("output.pdf")