import xml.etree.ElementTree as ET
from pathlib import Path


def load_data_file(file: Path):
    tree = ET.parse(file)
    output_list = []
    word = tree.getroot().tag.strip().split(".")[0]
    for i, tag in enumerate(tree.iter()):
        if i == 0:
            continue
        sentence = tag.text
        if sentence is None:
            continue
        words = sentence.split(" ")
        if word not in words:
            continue
        output_list.append({"word": word, "sentence": words})
    return output_list
