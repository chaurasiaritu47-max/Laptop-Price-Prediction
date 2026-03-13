import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re


# Setting the default encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

#columns for the data
Product_name = []
Prices = []
Description = []
Reviews = []
urls = []

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def data_scrape():
    global Product_name, Prices, Description, Reviews , urls
    for i in range(1,44):
        url = f"https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'lxml')
        main_div = soup.find('div',class_ = 'DOjaWF gdgoEp')
        product_names_div = main_div.find_all('div', class_ = 'KzDlHZ')
    # print(product_names_div)
        for each in product_names_div:
            names = each.text
            Product_name.append(names)
    # print(Product_name)  
 
        prices_div = main_div.find_all('div', class_ = 'Nx9bqj _4b5DiR')  
        for each in prices_div:
            prices = each.text
            price_number = re.findall(r'\d+', prices)  # Extract only numbers
            Prices.append("".join(price_number))  
    # print(Prices)     

        dscrptn_div = main_div.find_all('ul', class_ = 'G4BRas')
        for each in dscrptn_div:
            dptn = each.text
            Description.append(dptn)
    # print(Description)    

        reviews = main_div.find_all('div', class_ = 'XQDdHH')
        for each in reviews:
            rev = each.text
            Reviews.append(rev)
    # print(Reviews)  
        url_tags = main_div.find_all('a', class_='CGtC98')  
        extracted_urls = []  # Use a separate list to store extracted URLs

        for each in url_tags:
            if 'href' in each.attrs:  # Ensure 'href' exists
                link = "https://www.flipkart.com" + each['href']
                extracted_urls.append(link)  

        urls.extend(extracted_urls)

# dataFrame = pd.DataFrame({"Product_name": Product_n   ame , "Prices": Prices , "Description": Description , "Reviews": Reviews})
# dataFrame.to_csv("mobile_data1.csv")
    max_length = max(len(Product_name), len(Prices), len(Description), len(Reviews), len(urls))

    Product_name += [None] * (max_length - len(Product_name))
    Prices += [None] * (max_length - len(Prices))
    Description += [None] * (max_length - len(Description))
    Reviews += [None] * (max_length - len(Reviews))
    urls += [None] * (max_length - len(urls))

    df = pd.DataFrame({
        "Product_name": Product_name,
        "Prices": Prices,
        "Description": Description,
        "Reviews": Reviews,
        "urls": urls
    })


    df["Product_name"] = df["Product_name"].astype(str)
    df['Brand'] = df['Product_name'].str.split().str[0]

# Extract Processor Type 
    df['Processor_Type'] = df['Description'].str.extract(r'((Intel|AMD) \w+ \w+)')[0]
    df['RAM_Size'] = df['Description'].str.extract(r'(\d+ GB \w+ RAM)')[0]
    storage_extract = df['Description'].str.extract(r'(\d+\s*(GB|TB))\s*(SSD|HDD)', expand=True)

# Assign the split columns to new columns
    df['Storage_Capacity'] = storage_extract[0]
    df['Storage_Type'] = storage_extract[2]

    df['Storage_Capacity'].fillna('Not Available', inplace=True)
    df['Storage_Type'].fillna('Not Available', inplace=True)
    df['Screen_Size'] = df['Description'].str.extract(r'(\d+\.\d+ cm)')[0]

# Convert Screen Size from cm to inches 
    df['Screen_Size_Inches'] = (df['Screen_Size'].str.extract(r'(\d+\.\d+)').astype(float) / 2.54).round(2)
    df.drop(columns=['Screen_Size'], inplace=True)

# Extract Operating System (e.g., Windows 10, macOS, Linux)
    df['Operating_System'] = df['Description'].str.extract(r'(Windows \d+|macOS|Linux)')[0]
    df['Processor_Generation'] = df['Description'].str.extract(r'(\d+th Gen)')[0]
    df.fillna('Not Available', inplace=True)

    # Drop unwanted columns
    df.drop(columns=['Product_name','Description'], inplace=True, errors='ignore')

    df.to_csv("D:/Laptop_interface/final_laptop_datascrape.csv", index=False)

    driver.quit()
data_scrape()











# Function to get the next page link
# def get_next_page_url(soup):
#     next_page_tag = soup.find('a', class_='_9QVEpD')
#     if next_page_tag:
#         return "https://www.flipkart.com" + next_page_tag.get('href')
#     else:
#         return None

# for i in range(2, 12):
#     url = f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}"
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, "lxml")
#     next_page_url = get_next_page_url(soup)
#     if next_page_url:
#         print(next_page_url)
#     else:
#         print(f"Next page link not found on page {i}")

#driver.quit()


