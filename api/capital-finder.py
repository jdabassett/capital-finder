import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from datetime import datetime
import requests

class capitol_finder(BaseHTTPRequestHandler):

    def parse_url(self):
        str_url = self.path
        obj_url = parse.urlsplit(str_url)
        tup_queries = parse.parse_qsl(obj_url.query)
        dict_queries = dict(tup_queries)
        return dict_queries

    def parse_list(self,list_of_strings, str_conjunction = 'or'):
        if len(list_of_strings) == 1:
            return list_of_strings[0]
        else:
            return ", ".join(list_of_strings[:-1])+f', {str_conjunction} '+list_of_strings[-1]

    def make_request(self,dict_queries):
        str_country_query, str_capital_query = "", ""
        if 'country' in dict_queries and 'capital' in dict_queries:
            endpoint, value = 'name', dict_queries.get('country')
            str_country_query, str_capital_query = dict_queries.get('country').title(), dict_queries.get('capital').title()
        elif 'country' in dict_queries:
            endpoint, value = 'name', dict_queries.get('country')
        elif 'capital' in dict_queries:
            endpoint, value = 'capital', dict_queries.get('capital')
        else:
            return "Queries invalid, must supply country and/or capitol queries"


        # make get request
        str_url_name = f"https://restcountries.com/v3.1/{endpoint}/{value}?fields=name,capital,currencies,languages,population"
        obj_res = requests.get(str_url_name)

        # select most populous country from returned list
        dict_data = sorted(obj_res.json(), key=lambda x: x['population'], reverse=True)[0]

        # extract country
        str_country = dict_data.get('name').get('common').title()
        # extract capital
        str_capital = self.parse_list([i.title().replace(".","") for i in dict_data.get('capital')],"and")
        # extract languages
        str_languages = self.parse_list([j.title() for k,j in dict_data.get('languages').items()])
        # extract currencies
        str_currencies = self.parse_list([value.get('name').title() for key,value in dict_data.get('currencies').items()])

        # formate possible return strings
        dict_return = {}
        dict_return['country'] = f"The capital{'s' if 'and' in str_capital else ''} of {str_country} {'are' if 'and' in str_capital else 'is'} {str_capital}."
        dict_return['capital_country'] = f"True, {str_capital} is the capital of {str_country}." if (str_country_query==str_country and str_capital_query==str_capital) else f"False, {str_capital_query} is not the capital of {str_country_query}."
        dict_return['capital'] = f"{str_capital} {'are' if 'and' in str_capital else 'is'} the capital{'s' if 'and' in str_capital else ''} of {str_country}."
        dict_return['languages'] = f"People in {str_country} might speak {str_languages}."
        dict_return['currencies'] = f"People in {str_country} might pay with the {str_currencies}."

        # if country and capital in query, only return boolean response
        if 'country' in dict_queries and 'capital' in dict_queries:
            del dict_queries['country']
            del dict_queries['capital']
            del dict_queries['languages']
            del dict_queries['currencies']
            dict_queries['capital_country']=True

        return "\n".join([dict_return[key] for key,value in dict_queries.items()])

    def do_GET(self):
        # parse the url query parameters into a dictionary
        dict_queries = self.parse_url()

        # make different http requests based on parameters
        str_response = self.make_request(dict_queries)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str_response.encode('utf-8'))
        return

if __name__ == '__main__':
    server_address = ('localhost',8000)
    httpd = HTTPServer(server_address,capitol_finder)
    print(f"Starting httpd server on {server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

