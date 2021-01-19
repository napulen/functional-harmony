import music21
import os

def process(input, output):
    s = music21.converter.parse(input)
    tminus = 0
    for n in s.flat.notes:
        if n.measureNumber == 1:
            tminus = n.offset
            break
    with open(output, "w") as fout:
        for n in s.flat.notes:
            st = f"{n.offset - tminus},{n.pitch.midi},0,{n.quarterLength},0,0\n"
            fout.write(st)


for root, folders, files in os.walk("BPS_FH_Dataset_Augmentation"): 
    xmls = [f for f in files if f.endswith(".xml")] 
    for xml in xmls:
        print(os.path.join(root, xml))
        if "closeposition" in xml:
            filename = "notes_aug_closeposition.csv"
        else:
            filename = "notes_aug.csv"
        process(
            os.path.join(root, xml), 
            os.path.join(root, filename)
        )