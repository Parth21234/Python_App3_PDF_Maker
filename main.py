from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
# The page should not auto break.

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100, 100, 100) # Grey, values for r,g,b.
    # For red, 254,0,0.
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    # The arguments of the line method will be x1,y1,x2,y2.

    # Set the footer.
    pdf.ln(265) # Adding 265 break lines, each of 1 mm.

    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='R')

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer.
        pdf.ln(277)  # Adding 277 break lines, each of 1 mm.

        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align='R')

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

# border = 1 is for the box around the texts.
# ln is actually a break line.
# height 'h' has to be set as same as size of the font/text.

pdf.output("output.pdf")