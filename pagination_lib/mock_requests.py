from requests import Response
from requests.exceptions import Timeout
import json

def get(url, data=None, headers={}):
    """ Mock a response for requesting first or second page of a list of messages in a room, 
    depending on the passed url value. Three messages per page. """
    url_second_page = 'https://api.ciscospark.com/v1/messages?roomId=Y2lzY29zcGFyazovR1&max=3&beforeMessage=Y2lzY29zcGFyazovI4'
    response_file = './lib/webex_teams_response_page2.json' if url == url_second_page else './lib/webex_teams_response_page1.json'
    headers_file = 'webex_teams_response_headers.json'    
    response = Response()
    response.status_code = 200
    # response._content = b'TIMEOUT'
    with open(response_file,'r') as f:
        mock_response = f.read()
    response._content = mock_response.encode()
    # response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    response.headers['Link'] = f'<{url_second_page}>; rel= "next"'
    # raise Timeout('Timeout connecting to server')
    return(response)


if __name__ == '__main__':
    pass
