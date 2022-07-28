from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, letter, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Image,
)

Elements = []

# container for the 'Flowable' objects

doc = SimpleDocTemplate(
    "hellocomp.pdf",
    pagesize=letter,
)

styleSheet = getSampleStyleSheet()

I = Image("ModsDejaVu.jpg")
I.drawHeight = 1.25 * inch * I.drawHeight / I.drawWidth
I.drawWidth = 1.25 * inch
P0 = Paragraph(
    """
A paragraph
1""",
    styleSheet["BodyText"],
)
P = Paragraph(
    """ The ReportLab Left
Logo
Image""",
    styleSheet["BodyText"],
)

data = [
    ["A", "B", "C", P0, "D"],
    ["00", "01", "02", [I, P], "04"],
    ["10", "11", "12", [P, I], "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"],
]

t = Table(
    data,
    style=[
        ("GRID", (1, 1), (-2, -2), 1, colors.green),
        ("BOX", (0, 0), (1, -1), 2, colors.red),
        ("LINEABOVE", (1, 2), (-2, 2), 1, colors.blue),
        ("LINEBEFORE", (2, 1), (2, -2), 1, colors.pink),
        ("BACKGROUND", (0, 0), (0, 1), colors.pink),
        ("BACKGROUND", (1, 1), (1, 2), colors.lavender),
        ("BACKGROUND", (2, 2), (2, 3), colors.orange),
        ("BOX", (0, 0), (-1, -1), 2, colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("VALIGN", (3, 0), (3, 0), "BOTTOM"),
        ("BACKGROUND", (3, 0), (3, 0), colors.limegreen),
        ("BACKGROUND", (3, 1), (3, 1), colors.khaki),
        ("ALIGN", (3, 1), (3, 1), "CENTER"),
        ("BACKGROUND", (3, 2), (3, 2), colors.beige),
        ("ALIGN", (3, 2), (3, 2), "LEFT"),
    ],
)
t._argW[3] = 1.5 * inch

Elements.append(t)

# write the document to disk

doc.build(Elements)
