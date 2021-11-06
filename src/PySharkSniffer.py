import pyshark

outputPath = "d:\Documents\github\ParentControl\packets\"

cap = pyshark.FileCapture(outputPath + "\capturedPackets.cap")
capprint(cap[0])