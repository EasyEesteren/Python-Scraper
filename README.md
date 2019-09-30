# Python-Scraper
A python scraper for searching the frequency with which certain terms appear on webpages. Employees
the requests and csv modules.

This scraper requires the user to provide the URL of the desired webpage and the term/ terms which
they wish to know the frequency of. The scraper first prompts the user to input the URL, it then 
downloads and saves the webpage as "page.txt". The user is then again prompted to provide the name
of the .csv file they wish their results to be saved in. If the file does not exist it will be create
automatically, else new searches will simply be appended to the .csv file.

The user may keep searching for different terms as many times as they want. Each new search will be 
added to the .csv file.

This scraper is primarily intended for use in academia, where searching the frequency with which 
certain terms appear in newspapers or journals is often used in models in discplines such as
economics. Mannually gathering data on the frequency with which these terms appear can be time 
consuming and tiedious. This script hopes to remove this problem.
