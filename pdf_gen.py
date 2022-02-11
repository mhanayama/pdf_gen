# -*- coding: utf-8 -*-

import os
import argparse
import img2pdf
import tqdm
from natsort import natsorted

def pdf_gen(src, dst):
    pages = []
    for file in natsorted(os.listdir(src)):
        if os.path.splitext(file)[-1] == '.jpg' or os.path.splitext(file)[-1] == '.jpeg' or os.path.splitext(file)[-1] == '.png':
            pages.append(os.path.join(src, file))
    if len(pages) == 0:
        print("Failed: {}".format(src))
        return
    with open(dst, 'wb') as pdf:
        pdf.write(img2pdf.convert(pages))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src', help='src dir')
    args = parser.parse_args()

    dirs = [f.path for f in os.scandir(args.src) if f.is_dir()]

    # for dir in tqdm.tqdm(dirs):
    for dir in dirs:
        print(dir)
        pdf_gen(dir, '{}.pdf'.format(dir))
