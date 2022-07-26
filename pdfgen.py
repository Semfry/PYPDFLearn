from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, letter, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

my_text = "Hello\nThis is a <strong>multiline</strong> text\nHere we do not have to handle the positioning of each line manually"
Elements = []

# Text1 = (
#    Paragraph(my_text.replace("\n", "<br />"), getSampleStyleSheet()["Normal"]),
# )

doc = SimpleDocTemplate(
    "hello.pdf",
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm,
)

data = [
    ["00", "01", "02", "03", "04"],
    ["10", "11", "12", "13", "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"],
]
t = Table(data, 5 * [0.4 * inch], 4 * [0.4 * inch])
t.setStyle(
    TableStyle(
        [
            ("ALIGN", (1, 1), (-2, -2), "RIGHT"),
            ("TEXTCOLOR", (1, 1), (-2, -2), colors.red),
            ("VALIGN", (0, 0), (0, -1), "TOP"),
            ("TEXTCOLOR", (0, 0), (0, -1), colors.blue),
            ("ALIGN", (0, -1), (-1, -1), "CENTER"),
            ("VALIGN", (0, -1), (-1, -1), "MIDDLE"),
            ("TEXTCOLOR", (0, -1), (-1, -1), colors.green),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
            ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
Elements.append(
    Paragraph(my_text.replace("\n", "<br />"), getSampleStyleSheet()["Normal"])
)
Elements.append(t)

doc.build(Elements)
