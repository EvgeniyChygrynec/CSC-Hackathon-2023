import csv, os, markdown, re
from bs4 import BeautifulSoup

def create_csv(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['question', 'answer'])

        
        for filename in os.listdir(input_folder):
            if filename.endswith('.md'):
                filepath = os.path.join(input_folder, filename)


                with open(filepath, 'r', encoding='utf-8') as article_file:
                    text = article_file.read()
                    html = markdown.markdown(text)


                match = re.search(r'description:\s*(.*)', html, re.IGNORECASE)
                if match:
                    description = match.group(1)
                    description = description.strip()
                    description = description[:-4]
                soup = BeautifulSoup(text, 'html.parser')
                text = soup.find_all('p')
                if '#' in text:
                        text = text.split('#', 1)[1]
                text = text.replace('\n', '').replace('*', '').replace('#', '')
                text = text.replace('{{ company_name }}', 'Revenue Grid').replace('{{ product_name }}', 'RG Email Sidebar').replace('{{ short_name }}', 'RGES').replace('{{ short_company_name }}', 'RG')
                text = text.replace('\xa0', '').replace('\xa1\\', '').replace('\xa2\\', '').replace('\\.\t', '').replace('\t', '').replace("\'", "'")
                text = re.sub(r"\d+ min read - updated few hours ago", "", text)
                text = re.sub(r"\d+ min read", "", text)
                writer.writerow([description, text])

# Укажите путь к папке со статьями и путь к создаваемому CSV-файлу
input_folder = 'C:\\Users\\Yulia\\Desktop\\MINIChatGPT\\SfccDocs\\src\\articles'
output_file = 'C:\\Users\\Yulia\\Desktop\\MINIChatGPT\\knowledge_base.csv'

create_csv(input_folder, output_file)