import requests, bs4, json, pandas, csv
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

# Choose whether to Get Json data from Plymouth Data site

print("Gather Park data from Plymouth site?")
parkDownChoice = input().lower()
x = "true"
while x == "true":
    if parkDownChoice == "yes":
        plyDataArrive = requests.get(
            "https://plymouth.thedata.place/dataset/479dd1bd-3b15-4640-a259-32b2c440445b/resource/cda4367c-090f-42e7-80ae-827b19e3fc07/download/peoplecount-arrival.geojson"
        )
        plyDataArrive.raise_for_status
        plyData = open("parkarrivedata.json", "wb")
        for chunk in plyDataArrive.iter_content(100000):
            plyData.write(chunk)

        plyData.close()
        break
    elif parkDownChoice == "no":
        print("continuing to next section...")
        break
    else:
        print("Please enter yes or no")
        parkDownChoice = input().lower()

# ----------------------------------------------------
# Base PDF Settings for Reportlab

elements = []

plyDoc = SimpleDocTemplate(
    "Plydata.pdf",
    pagesize=A4,
)

styleSheet = getSampleStyleSheet()

# ----------------------------------------------------
# Make PDF from data

# with open("parkarrivedata.json", "r") as parkJson:
#     parkData = json.load(parkJson)
# summary = [["Age", "Activity"]]
# for i in range(len(parkData["features"])):
#     agesp = parkData["features"][i]["properties"]["Age"]

#     P0 = Paragraph(
#         agesp,
#         styleSheet["BodyText"],
#     )

#     activityp = parkData["features"][i]["properties"]["Activity"]

#     P1 = Paragraph(
#         activityp,
#         styleSheet["BodyText"],
#     )
#     summary.append([P0, P1])

with open("parkarrivepandas.csv", "r") as parkJson:
    parkData = csv.reader(parkJson)
    summary = [["Age", "Activity"]]
    for i in parkData:
        agesp = parkData["Age"]

        P0 = Paragraph(
            agesp,
            styleSheet["BodyText"],
        )

        activityp = parkData["Activity"]

        P1 = Paragraph(
            activityp,
            styleSheet["BodyText"],
        )
        summary.append([P0, P1])

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
