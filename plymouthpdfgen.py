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
from rich.pretty import pprint

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

# with open("ancienttrees.json", "r") as parkJson:
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

P0 = 0
P1 = 1

# with open("ancienttrees.json") as parkJson:
parkJson = open("ancienttrees.json")
treeSpecImage = Image("treespec.jpg", 2*inch, 2*inch)
treeLiveImage = Image("treelive.jpg", 2*inch, 2*inch)

parkData = json.load(parkJson)

summary = [[treeSpecImage, treeLiveImage]]

# for k, v in parkData.items():
#     agesp = parkData["SPECIES"]
#     for count, age in agesp.items():

#         P0 = Paragraph(
#             age,
#             styleSheet["BodyText"],
#         )
#         summary.append([P0])

# activityp = parkData["Activity"]
# for count, activity in activityp.items():

#     P1 = Paragraph(
#         activity,
#         styleSheet["BodyText"],
#     )
#     summary.append([P1])

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
