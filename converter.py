import csv
import time
import xml.etree.ElementTree as ET
from tqdm import tqdm

INPUT_FILE = "large_data.xml"
OUTPUT_FILE = "data_converted.csv"

CSV_HEADERS = ['id', 'name', 'category', 'price', 'stock']

def convert_xml_to_csv(xml_file, csv_file):
    print(f"Starting: {xml_file} -> {csv_file}")
    start_time = time.time()
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        
        writer.writerow(CSV_HEADERS)
        
        context = ET.iterparse(xml_file, events=("end",))
        context = iter(context)
        _, root = next(context)
        
        count = 0

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
                        count += 1
                        pbar.update(1)
                    except AttributeError:
                        pass

                    elem.clear()
                    root.clear()

    end_time = time.time()
    duration = end_time - start_time
    print(f"Success! Executed {count} items for {duration:.2f} seconds")

if __name__ == "__main__":
    convert_xml_to_csv(INPUT_FILE, OUTPUT_FILE)