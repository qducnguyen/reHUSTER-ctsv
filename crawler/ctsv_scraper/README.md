1. Get config.py from ducnq
2. At /crawler/ctsv_scraper: Run
    - scrapy crawl activities_ctsv -o output/activities.jsonl
    - scrapy crawl user_activities_ctsv -o output/user_activities.jsonl 