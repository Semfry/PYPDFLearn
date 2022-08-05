import requests, sys, webbrowser, bs4, json
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

# Get data from Plymouth Data site and open as JSON

plyDataArrive = requests.get(
    "https://plymouth.thedata.place/dataset/479dd1bd-3b15-4640-a259-32b2c440445b/resource/cda4367c-090f-42e7-80ae-827b19e3fc07/download/peoplecount-arrival.geojson"
)
plyDataArrive.raise_for_status
plyData = open("parkarrivedata.json", "wb")
for chunk in plyDataArrive.iter_content(100000):
    plyData.write(chunk)

plyData.close()

# Make PDF from data (ID, Age, Activity)

elements = []

plyDoc = SimpleDocTemplate(
    "Plydata.pdf",
    pagesize=A4,
)

styleSheet = getSampleStyleSheet()

with open("parkarrivedata.json") as parkJson:
    parkData = json.load(parkJson)

summary = [["Age", "Activity"]]
for i in range(len(parkData["features"])):
    agesp = parkData["features"][i]["properties"]["Age"]

    P0 = Paragraph(
        agesp,
        styleSheet["BodyText"],
    )
    activityp = parkData["features"][i]["properties"]["Activity"]

    P1 = Paragraph(
        activityp,
        styleSheet["BodyText"],
    )

    summary.append([P0, P1])

elements = []

plyP = Table(
    summary,
    style=[
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BOX", (0, 0), (-1, -1), 2, colors.black),
    ],
)

elements.append(plyP)

plyDoc.build(elements)

# Close open files

parkJson.close()
