# -*- coding:utf-8 -*-

from tika import parser


def _pdf2text(input_file, output_file):

    data = parser.from_file(input_file)
    content = data['content']

    with open(output_file, mode='w') as textfile:

        print(content)
        textfile.write(content)
