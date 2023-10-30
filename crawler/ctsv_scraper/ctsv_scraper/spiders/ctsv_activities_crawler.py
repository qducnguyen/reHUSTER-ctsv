from typing import Any, Iterable
import scrapy
import json

from scrapy.http import Request, Response
from .config import headers, cookies, activities_body

class CTSVActivitySpider(scrapy.Spider):
    name = "activities_ctsv"
    allowed_domains=["ctsv.hust.edu.vn"]
    url = 'https://ctsv.hust.edu.vn/api-t/Activity/GetActivityById'

    headers = headers
    cookies = cookies    
    body = activities_body 

    min_acitivites_id = 0
    expected_maximum_acitivites_id = 8900

    def start_requests(self) -> Iterable[Request]:
        for i in range(self.min_acitivites_id, self.expected_maximum_acitivites_id):
            
            body = self.body.format_map({"AId": i})
            yield Request(
                    url=self.url,
                    method='POST',
                    dont_filter=True,
                    cookies=self.cookies,
                    headers=self.headers,
                    body=body,
                    cb_kwargs={"AId": i}

                )
        

    def parse(self, response: Response, AId):
        data = json.loads(response.text)
        data.update({"AId": AId})
        yield data