import requests

# Choose whether to Get Json data from Plymouth Data site

print("Gather Ancient Tree data from Plymouth site?")
parkDownChoice = input().lower()
x = "true"
while x == "true":
    if parkDownChoice == "yes" or "y":
        plyDataArrive = requests.get(
            "https://plymouth.thedata.place/dataset/a3464bbf-4063-4127-a3b4-00cb136be654/resource/390e24e5-c818-4967-b42c-29f343fb21c8/download/ancient-trees.geojson"
        )
        plyDataArrive.raise_for_status
        plyData = open("ancient-trees.geojson", "wb")
        for chunk in plyDataArrive.iter_content(100000):
            plyData.write(chunk)

        plyData.close()
        break
    elif parkDownChoice == "no" or "n":
        print("continuing to next section...")
        break
    else:
        print("Please enter yes or no")
        parkDownChoice = input().lower()
