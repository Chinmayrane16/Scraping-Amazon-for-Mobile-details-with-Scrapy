# Scraping-Amazon-for-Mobiles-details-with-Scrapy

In this repository I have build an Amazon scraper for extracting Mobile details and pricing using a python framework called scrapy.
I have used Pycharm IDE and I have extracted the following details for 5 pages on the Amazon site.<br>
1) Mobile Name
2) Mobile Reviews
3) Mobile Prices
4) Mobile Imagelinks

After extracting the information, I have saved it into a JSON file.

## Requirements

* [Pycharm](https://www.jetbrains.com/pycharm/) - The first requirement is a software to run the script.<br>
* [Scrapy](https://scrapy.org/) = 1.6.0
* [pypiwin32](https://pypi.org/project/pypiwin32/) = 224
* [scrapy-user-agents](https://pypi.org/project/scrapy-user-agents/) = 0.1.1

## Implementation

After installing Pycharm IDE, create a new project File->New Project<br>
Install the requirements File->Settings->Project->Project Interpreter->(Click + symbol)->(package name)->Install<br>

After installing the packages open terminal at the bottom left corner and type `scrapy startproject projectname` you can see the following files added to your project.<br>
<pre>
.
--- amazonscrap
|   --- __init__.py
|   --- items.py
|   --- middlewares.py
|   --- pipelines.py
|   --- settings.py
|   --- spiders
|     --- __init__.py
--- scrapy.cfg
</pre>

Go to the [items.py](https://github.com/Chinmayrane16/Scraping-Amazon-for-Mobiles-data-and-Pricing-with-Scrapy/blob/master/Amazon_Mobile_Details/items.py) and add the fields you want to extract.<br>
Go to the your [projectspider.py](https://github.com/Chinmayrane16/Scraping-Amazon-for-Mobiles-data-and-Pricing-with-Scrapy/blob/master/Amazon_Mobile_Details/spiders/amazon_spider.py) and extract the details from the webpage by inspecting the page and locate the css class and copy and add it to your code.<br>
Pass the variables containing the details to the items dictionary.

When your are done with the coding part, now you're ready to run the script. But to prevent Amazon from blocking you, you could use the following tricks to bypass their security measures.<br>
1) **GoogleBot** - Confuse the site by faking your user-agent to be google's bot agent. Amazon allows access to google to crawl it's website. Add the code to your `settings.py` -> `USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'`

2) **Rotating User-Agents and Spoofing** - Spoof the User Agent by creating a list of user agents and picking a random one for each request. Websites do not want to block genuine users so you should try to look like one. Add the code to your `settings.py` -> `DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}`

3) **Rotating IPs and Proxy Services** - Use different IP addresses for making requests to a server, so that the detection becomes harder. Create a pool of IPs that you can use and use random ones for each request. We can use VPNs, shared proxies for the same.


Finally run the project on the terminal using the command `scrapy crawl spidername` and you can see the responses on the terminal.
To generate json file with the responses run the command `scrapy crawl spidername -o items.json`. A JSON file will be created with the name ["items.json"](https://github.com/Chinmayrane16/Scraping-Amazon-for-Mobiles-data-and-Pricing-with-Scrapy/blob/master/items.json).
