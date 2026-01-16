import random
import time

FILENAME = "large_data.xml"
TOTAL_RECORDS = 500_000 

CATEGORIES = ["Electronics", "Books", "Clothing", "Home & Garden", "Toys", "Sports"]
ADJECTIVES = ["Super", "Awesome", "Cheap", "Luxury", "Smart", "Old-school", "Future"]
NOUNS = ["Phone", "Book", "T-Shirt", "Sofa", "Robot", "Ball", "Laptop"]

def generate_xml(filename, count):
    print(f"Starting generation of {count} items into the file '{filename}'...")
    start_time = time.time()
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<catalog>\n')
        
        for i in range(count):
            p_id = i + 1
            p_name = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)} {random.randint(100, 999)}"
            p_category = random.choice(CATEGORIES)
            p_price = round(random.uniform(5.0, 2000.0), 2)
            p_stock = random.randint(0, 1000)
            
            record = (
                f'  <product id="{p_id}">\n'
                f'    <name>{p_name}</name>\n'
                f'    <category>{p_category}</category>\n'
                f'    <price currency="USD">{p_price}</price>\n'
                f'    <stock>{p_stock}</stock>\n'
                f'  </product>\n'
            )
            f.write(record)
            
            if (i + 1) % 50_000 == 0:
                print(f"   -> Executed {i + 1} items...")

        # Закрываем корневой тег
        f.write('</catalog>')
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Done! File created for {duration:.2f} seconds")

if __name__ == "__main__":
    generate_xml(FILENAME, TOTAL_RECORDS)