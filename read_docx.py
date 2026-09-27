import zipfile
import xml.etree.ElementTree as ET
import sys

def read_docx(path):
    try:
        z = zipfile.ZipFile(path)
        tree = ET.fromstring(z.read('word/document.xml'))
        text = []
        for node in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            text.append(''.join(node.itertext()))
        return '\n'.join(text)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(read_docx(sys.argv[1]))
