from selenium import webdriver
import time
import re

# Function to retrieve the complaint content and publication date from a given URL
def get_comp(url):
    driver.get(url)  # Load the webpage

    comp_source = driver.page_source  # Get the source code of the page

    # Regular expression to find the complaint content within the page's source code
    comp_patern = r'articleBody":"([^"]+)"'
    comp = re.findall(comp_patern, comp_source)  # Extract the complaint content

    try:
        # Regular expression to find the publication date of the complaint
        pub_patern = r'<div class="js-tooltip time" title="([^"]+)'
        try:
            pub_date = re.findall(pub_patern, comp_source)  # Extract the publication date
            pub_date = pub_date[0]  # Get the first match
        except:
            pub_date = 'Unknown'  # Default value if the publication date is not found

        return comp[0], pub_date  # Return the complaint content and publication date

    except(IndexError):
        return False  # Return False if the complaint content is not found


# Function to get a list of complaint URLs from the main page
def get_comp_list(main_page, driver):
    driver.get(main_page)  # Load the main page
    time.sleep(1)  # Wait for the page to fully load

    source = driver.page_source  # Get the source code of the page

    # Regular expression to find complaint URLs in the page's source code
    link_patern = r'mainEntityOfPage":"([^"]+)"'
    result = re.findall(link_patern, source)  # Extract all complaint URLs

    return result  # Return the list of complaint URLs


# Setup Selenium WebDriver options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress logging messages

driver = webdriver.Chrome(options=options)  # Initialize the WebDriver
page_count = 0  # Initialize the page counter
total = 0  # Initialize the total complaints counter
all_links = []  # Initialize a list to store all complaint URLs

print('Searching URLs...')

# Loop through the first 10 pages of complaints
while page_count <= 10:
    page_count += 1
    main_page = f'https://www.sikayetvar.com/sikayetler?page={str(page_count)}'  # Construct the URL for each page

    result = get_comp_list(main_page, driver)  # Get the list of complaint URLs from the page
    for i in result:
        all_links.append(i)  # Add each URL to the list

# Remove duplicate URLs from the list
all_links = list(set(all_links))

print(f'{len(all_links)} URLs found...')

# Loop through each unique complaint URL
for url in all_links:
    if 'https://www.sikayetvar.com/sikayetler' != url:  # Skip the main page URL itself
        complaint = get_comp(url)  # Get the complaint content and publication date
        
        if complaint:
            with open('sikayetvar_data.txt', 'a', encoding='UTF-8') as file:
                total += 1
                # Write the complaint number, publication date, URL, and complaint content to the file
                file.write(f'{total}|{complaint[1]}|{url}|{complaint[0]}\n')
