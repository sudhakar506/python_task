from requests import get, post, exceptions
import json
import time
from config import config

class Task:
    def __init__(self):
        self.headers = {"accept": "application/json", "content-type": "application/json"}
        self.payload = {"technology": "Python", "domain": "healthcare"}
        self.base_url = "https://httpbin.org/"
        self.get_url = "get"
        self.post_url = "post"
        self.delay_time = 5
        self.user = config.USER
        self.pwd = config.PWD
    
    def get_response(self):
        try:
            response = get(f"{self.base_url}/{self.get_url}", headers=self.headers)
            return f"Get Response : {response.status_code}"
        except exceptions.RequestException as e:
            return e
        
        
    def post_response(self):
        try:
            response = post(f"{self.base_url}/{self.post_url}", headers=self.headers, data = json.dumps(self.payload))
            if response.status_code == 200:
                api_response = response.json()
                required_result = json.loads(api_response['data'])['technology']
                if required_result == self.payload['technology']:
                   return "Post Response with valid payload info"
                else:
                   return "Post response is invalid"
            else:
                return response.status_code
        except exceptions.RequestException as e:
            return e
    
    def post_delay(self):
        headers = {"accept": "application/json", "content-type": "application/json"}
        payload = {"technology": "Python", "domain": "healthcare"}

        try:
            start_time = time.time()
            response = post(f"{self.base_url}/delay/{self.delay_time}", data=json.dumps(payload))
            end_time = time.time()
            total_time = end_time - start_time
            if response.status_code == 200:
                return f"Delay Time : {total_time}"
            
            else:
                return response.status_code, '', ''
                
        except exceptions.RequestException as e:
            return e
    
    def get_authentication(self):
        try:
            response = get(f"{self.base_url}/basic-auth/", auth=(self.user, self.pwd), headers=self.headers)
            return "Get Response with success authentication"
        except exceptions.RequestException as e:
            return f"Get Response with success authentication.{e}"
    
    def get_unautherized(self):
        try:
            response = get(f"{self.base_url}/basic-auth/python2/python%40123", auth=(self.user, self.pwd))
            return f"Unauthorized Access : {response.status_code}"
        except exceptions.RequestException as e:
           return f"Unauthorized Access : {response.status_code}"
    
    def page_not_found(self):
        try:
            response = post(f"{self.base_url}/basic-auth/test/")
            return f"Negative Scenario : {response.status_code}"
        except exceptions.RequestException as e:
           return f"Negative Scenario : {response.status_code}"

if __name__ == '__main__':
    obj = Task()
    print(obj.get_response())
    print(obj.post_response())
    print(obj.post_delay())
    print(obj.get_authentication())
    print(obj.get_unautherized())
    print(obj.page_not_found())
