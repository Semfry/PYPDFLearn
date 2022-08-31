import requests, json, pandas, collections, geopandas, matplotlib.pyplot as plt, contextily as cx

# Load Data

with open("ancient-trees.geojson") as data_file:
    plyPan = geopandas.read_file(data_file)

# Edit Data

# Compare data

# plyPan.crs

# Make Graphs

# plyPan

ax = plyPan.plot(
    "SPECIES",
    figsize=(20, 20),
    alpha=0.8,
    legend=True,
    legend_kwds={"loc": "upper right", "bbox_to_anchor": (1.13, 1)},
)
cx.add_basemap(ax, crs=plyPan.crs)
ax.set_axis_off()

plt.savefig("treespec.jpg")

ax = plyPan.plot(
    "LIVING_STA",
    figsize=(20, 20),
    alpha=0.8,
    legend=True,
    legend_kwds={"loc": "upper right", "bbox_to_anchor": (1, 1)},
)
cx.add_basemap(ax, crs=plyPan.crs)
ax.set_axis_off()

plt.savefig("treelive.jpg")

# plyPan.explore(
#                "SPECIES",
#                legend=True
#                )

# Write data to file

# plyPan.to_file("ancienttrees.json", Driver="json")
