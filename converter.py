import csv
import time
import os
import argparse
import xml.etree.ElementTree as ET
from tqdm import tqdm

import tkinter as tk
from tkinter import filedialog, messagebox

CSV_HEADERS = ['id', 'name', 'category', 'price', 'stock']

def get_files_via_gui():
    root = tk.Tk()
    root.withdraw()

    print("Waiting...")
    input_path = filedialog.askopenfilename(
        title="Which xml file do you want to convert?",
        filetypes=[("XML files", "*.xml"), ("All files", "*.*")]
    )
    
    if not input_path:
        print("Cancelled")
        return None, None

    print(f"   Выбран: {os.path.basename(input_path)}")

    output_path = filedialog.asksaveasfilename(
        title="Where to save CSV file?",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        initialfile="data_converted.csv"
    )

    if not output_path:
        print("Cancelled")
        return None, None

    return input_path, output_path

def convert_xml_to_csv(xml_file, csv_file):
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
    in_file, out_file = get_files_via_gui()
    
    if in_file and out_file:
        convert_xml_to_csv(in_file, out_file)