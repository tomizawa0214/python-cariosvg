from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

drawing = svg2rlg("101.svg")
renderPM.drawToFile(drawing, "file.png", fmt="PNG")