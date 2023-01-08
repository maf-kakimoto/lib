# -*- coding:utf-8 -*-

from docx import Document


def _f2f(input, output):

    data = Document(input)
    with open(output, mode='w') as f:
        for paragraph in data.paragraphs:
            f.write(paragraph.text+'\n')
