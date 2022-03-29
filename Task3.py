import requests
f = open("ServerList.txt", "r")
for x in f:
    print('URL is: '+ x)
    if x[-1] == '\n':
        headers = requests.get(x[:-1]).headers
        print('Headers are: ',headers)
        try:
            if headers['X-Frame-Options'] == 'DENY' or 'SAMEORIGIN':
                print('X-Frame-Options: '+'It is Safe')
            else:
                print('X-Frame-Options: '+'It is not safe')
        except:
            print('X-Frame-Options is not available')

        try:
            if headers['X-XSS-Protection'] == '0':
                print('X-XSS-Protection: '+'It is Safe')
            else:
                print('X-XSS-Protection: '+'It is not safe')
        except:
            print('X-XSS-Protection is not available')

        try:
            if headers['X-Content-Type Option'] == 'nosniff':
                print('X-Content-Type Option: '+'It is Safe')
            else:
                print('X-Content-Type Option: '+'It is not safe')
        except:
            print('X-Content-Type Option is not available')


    else:
        print('Headers are: ', headers)

        try:
            if headers['X-Frame-Options'] == 'DENY':
                print('X-Frame-Options: ' + 'It is Safe')
            else:
                print('X-Frame-Options: ' + 'It is not safe')
        except:
            print('X-Frame-Options is not available')

        try:
            if headers['X-XSS-Protection'] == '0':
                print('X-XSS-Protection: ' + 'It is Safe')
            else:
                print('X-XSS-Protection: ' + 'It is not safe')
        except:
            print('X-XSS-Protection is not available')

        try:
            if headers['X-Content-Type Option'] == 'nosniff':
                print('X-Content-Type Option: ' + 'It is Safe')
            else:
                print('X-Content-Type Option: ' + 'It is not safe')
        except:
            print('X-Content-Type Option is not available')

