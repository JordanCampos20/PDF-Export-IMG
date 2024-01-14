import pypdfium2 as pdfium
from pathlib import Path

default_folder = f"{Path(__file__).parents[1].resolve()}"

def convert(input, output):
    input_name, input_ext = input.split(".")
    output_name, output_ext = output.split(".")
    PDF = pdfium.PdfDocument(f"{default_folder}\\{input_name}.{input_ext}")
    n_pages = len(PDF)
    try:
        for page_number in range(n_pages):
            page = PDF.get_page(page_number)
            pil_image = page.render_topil(
                scale=300/72,
                rotation=0,
                crop=(0, 0, 0, 0),
                greyscale=False,
                optimise_mode=pdfium.OptimiseMode.NONE,
            )
            pil_image.save(f"{default_folder}\\{output_name}_{str(page_number+1).rjust(2, '0')}.{output_ext}")
    except Exception as ex:
        raise ex