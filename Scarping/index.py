from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    data = soup.find_all('div', class_='b')
    print(data)