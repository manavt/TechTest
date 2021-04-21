import requests
class RetrieveToken:

    def __init__(self):
        pass

    def get_api_token(self):
        headers = {'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
        response = requests.put('http://169.254.169.254/latest/api/token', headers=headers)
        if response.status_code == 200:
            return response.text
