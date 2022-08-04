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

# print("Compiling data")  # display text while downloading the page
plyDataArrive = requests.get(
    "https://plymouth.thedata.place/dataset/479dd1bd-3b15-4640-a259-32b2c440445b/resource/cda4367c-090f-42e7-80ae-827b19e3fc07/download/peoplecount-arrival.geojson"
)
plyDataArrive.raise_for_status
plyData = open("parkarrivedata.json", "wb")
for chunk in plyDataArrive.iter_content(100000):
    plyData.write(chunk)

plyData.close()

# Make PDF from data (ID, Age, Activity)

with open("parkarrivedata.json", "r") as parkJson:
    parkData = json.load(parkJson)
for i in range(len(parkData["features"])):
    # print(parkData["features"][i]["properties"]["Age"])
    agesp = parkData["features"][i]["properties"]["Age"]
    activityp = parkData["features"][i]["properties"]["Activity"]

# print(agesp)
# print(activityp)

parkDi = {}
parkDi.update({"Age": str(agesp)})
# parkDi.update({"Activity":str(activityp)})

elements = []

plyDoc = SimpleDocTemplate(
    "Plydata.pdf",
    pagesize=A4,
)

styleSheet = getSampleStyleSheet()

P0 = Paragraph(
    agesp,
    styleSheet["BodyText"],
)

P1 = Paragraph(
    activityp,
    styleSheet["BodyText"],
)

plyParkTable = [
    ["Age", "Activity"],
    [P0, P1],
    #["20", "21"],
    #["30", "31"],
]

plyP = Table(
    plyParkTable,
    style=[
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BOX", (0, 0), (-1, -1), 2, colors.black),
    ],
)
#plyP._argW[3] = 1.5 * inch

elements.append(plyP)

plyDoc.build(elements)

# Close open files

parkJson.close()
