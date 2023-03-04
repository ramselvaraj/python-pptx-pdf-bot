import os
import argparse
from tqdm import tqdm


def convert_pptx_to_pdf(filename):
    pdf_filename = os.path.splitext(filename)[0] + '.pdf'
    command = f'libreoffice --headless --convert-to pdf "{filename}" --outdir . >/dev/null 2>&1'
    os.system(command)
    os.rename(os.path.splitext(filename)[0] + '.pdf', pdf_filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store_true', help='convert all pptx files in the current directory to pdf')
    parser.add_argument('-f', metavar='filename', help='convert the specified pptx file to pdf')
    args = parser.parse_args()

    if args.a and args.f:
        print('Error: Cannot use both -a and -f flags at the same time')
        return

    pptx_files = []
    if args.a:
        pptx_files = [f for f in os.listdir() if f.endswith('.pptx')]
    elif args.f:
        if not args.f.endswith('.pptx'):
            print('Error: Specified file must have a .pptx extension')
            return
        pptx_files = [args.f]
    else:
        print('Error: Must specify either -a or -f flag')
        return

    total_files = len(pptx_files)
    with tqdm(total=total_files, desc='Converting files') as pbar:
        for i, filename in enumerate(pptx_files):
            pbar.set_description(f'Converting {filename}')
            convert_pptx_to_pdf(filename)
            pbar.update(1)

    print('Conversion complete!')


if __name__ == '__main__':
    main()
