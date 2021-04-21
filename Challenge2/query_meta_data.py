import requests
import argparse
from retrieve_token import RetrieveToken as token

class QueryMetaData:
    def __init__(self):
        self.token = token().get_api_token()
        self.headers = {'X-aws-ec2-metadata-token': self.token}
        self.url = 'http://169.254.169.254/latest/meta-data' 

    def retrive_meta_data(self):
        result = self.get(self.url, self.headers)
        return {'keys': result.text.split("\n")}  

    def retrive_individual_key_meta_data(self, meta_data_path):
        result = self.get(f'{self.url}/{meta_data_path}', self.headers)
        if result.status_code == 200:
            return {f'{meta_data_path}': result.text.split("\n")}
        else:
            return {f'{meta_data_path}': 'Not found'}

    def get(self, url, headers):
        response = requests.get(url, headers=headers)
        return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "query instance meta data")
    parser.add_argument("--key", "--individual-key-name", help = "individual path or key name")
    args = parser.parse_args()
    q = QueryMetaData()
    if args.key:
        print(q.retrive_individual_key_meta_data(args.key))
    else:
        print(q.retrive_meta_data())
