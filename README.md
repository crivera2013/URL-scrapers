# URL-scrapers
scrapes home pages from input list of companies using multiple search engines
This sample program takes a list of companies, and uses ip/user-agent masks, beautifulsoup and a quintet of search engines to source the home pages for a list of companies.
The program then outputs the list of companies and their urls into a new excel file.  Multiple urls are scraped and then fuzzy match compared to the company with the highest scored url then being inserted into the excel sheet.
