import csv
import time
import os
import argparse
import xml.etree.ElementTree as ET
from tqdm import tqdm

CSV_HEADERS = ['id', 'name', 'category', 'price', 'stock']

def convert_xml_to_csv(xml_file, csv_file):
    if not os.path.exists(xml_file):
        print(f"Error: File '{xml_file}' not found.")
        return

    file_size_mb = os.path.getsize(xml_file) / (1024 * 1024)
    print("-" * 40)
    print(f"Input file: {xml_file} ({file_size_mb:.2f} MB)")
    print(f"Output file: {csv_file}")
    print("-" * 40)
    start_time = time.time()
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        
        writer.writerow(CSV_HEADERS)
        
        context = ET.iterparse(xml_file, events=("end",))
        context = iter(context)
        _, root = next(context)
        
        with tqdm(total=None, unit=" rec", desc="Processing") as pbar:
            for event, elem in context:
                if elem.tag == "product":
                    try:
                        p_id = elem.attrib.get('id')
                        name = elem.find('name').text
                        category = elem.find('category').text
                        price = elem.find('price').text
                        stock = elem.find('stock').text
                        
                        writer.writerow([p_id, name, category, price, stock])
                        pbar.update(1)
                    except AttributeError:
                        pass

                    elem.clear()
                    root.clear()

    end_time = time.time()
    duration = end_time - start_time
    
    print("-" * 40)
    print(f"Success! Time of execution: {duration:.2f}/s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("input", help="Path to XML file")
    parser.add_argument("output", help="Path to CSV file")

    args = parser.parse_args()

    convert_xml_to_csv(args.input, args.output)