class CallChecker:
    def NoCheck(self,number):
        import requests
        url = "https://veriphone.p.rapidapi.com/verify"
        phone=number
        querystring = {"phone":phone}
        headers = {'x-rapidapi-key': "cf1779da82msh3be14dcb6cdd7e3p114573jsneeecbb22efd3",
        'x-rapidapi-host': "veriphone.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            d=(requests.request("GET", url, headers=headers, params=querystring).text)
            v=d[1:-2]
            b=(v.split(','))
            for x in b:
                print(x)
        except:
            print('This could not be found...')
    def SpamCheck(self,number):
        import requests
        url = "https://spamcheck.p.rapidapi.com/index.php"
        querystring = {"number":number}
        headers = {
            'x-rapidapi-key': "cf1779da82msh3be14dcb6cdd7e3p114573jsneeecbb22efd3",
            'x-rapidapi-host': "spamcheck.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            d=(requests.request("GET", url, headers=headers, params=querystring).text)
            v=d[1:-2]
            b=(v.split(','))
            for x in b:
                print(x.replace(' ',''))
        except:
            print('This could not be found...')

    
        