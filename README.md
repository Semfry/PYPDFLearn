# PYPDFLearn
# Learning reportlab for Python PDF

python -m venv venv

source venv/bin/activate # Linux

cd C:\GitHub\PYPDFLearning\venv\Scripts # Windows

.\activate

pip install -r requirements.txt

# Jupyter notebooks fix
modified py3k_compat.py by 8 string:
return isinstance(x, collections.Callable) -> return isinstance(x, collections.abc.Callable)

git commit -m "push message"

git push

git pull

black -l 80 pdfgen.py

black -l 80 pdfgen2.py

black -l 80 plymouthpdfgen.py

black -l 80 getdataplymouth.py

pipwin install gdal

pipwin install fiona

.\pdfgen

.\pdfgen2

https://www.blog.pythonlibrary.org/2010/09/21/reportlab-tables-creating-tables-in-pdfs-with-python/
