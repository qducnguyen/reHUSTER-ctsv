from typing import  Iterable
import scrapy
import json

from scrapy.http import Request, Response
from .config import headers, cookies, user_activities_body

class CTSVUserActivitySpider(scrapy.Spider):
    name = "user_activities_ctsv"
    allowed_domains=["ctsv.hust.edu.vn"]
    url = 'https://ctsv.hust.edu.vn/api-t/Activity/GetUserActivityByAId'

    headers = headers
    cookies = cookies    
    body = user_activities_body

    min_acitivites_id = 0
    expected_maximum_activites_id = 9085 # 18:17:00 23/12/22

    def start_requests(self) -> Iterable[Request]:
        for i in range(self.min_acitivites_id, self.expected_maximum_activites_id):
            
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