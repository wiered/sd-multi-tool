import os

import csv

def read_csv(filename) -> dict:
    if not filename:
        raise ValueError

    if not os.path.exists(filename):
        raise FileNotFoundError
    
    if not filename.endswith('.csv'):
        raise ValueError('not an .csv file')

    with open(filename, encoding="utf-8") as csv_file:
        line_count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        # if not headers == ['name', 'prompt', 'negative_prompt']:
        #     raise ValueError('Wrong csv file')
        
        styles = []
        for row in csv_reader:
            styles.append(row)
            line_count += 1

    return styles

def write_csv(filename, styles_list) -> None:
    with open(filename, mode='w', encoding="utf-8", newline='') as csv_file:
        headers = ['name', 'prompt', 'negative_prompt']
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for category in styles_list.categories:
            tmp = {'name': category._name, 'prompt': '', 'negative_prompt': ''}
            writer.writerow(tmp)
            for style in category.styles:
                tmp = {'name': style.name, 'prompt': style.prompt, 'negative_prompt': style.negative_prompt}
                writer.writerow(tmp)
            
            writer.writerow({})

            
