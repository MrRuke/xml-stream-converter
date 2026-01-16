import pytest
import os
import csv
from converter import convert_xml_to_csv

@pytest.fixture
def temp_files():
    input_file = "pytest_input.xml"
    output_file = "pytest_output.csv"
    
    xml_content = """<?xml version="1.0"?>
    <catalog>
        <product id="999">
            <name>Pytest Item</name>
            <category>Software</category>
            <price>0.00</price>
            <stock>1</stock>
        </product>
    </catalog>
    """
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    yield input_file, output_file
    
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)

def test_xml_conversion(temp_files):
    in_file, out_file = temp_files
    
    convert_xml_to_csv(in_file, out_file)
    
    assert os.path.exists(out_file) is True, "Файл CSV не был создан"
    
    with open(out_file, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        
        assert len(reader) == 2
        
        row = reader[1]
        assert row[0] == "999"
        assert row[1] == "Pytest Item"
        assert row[3] == "0.00"