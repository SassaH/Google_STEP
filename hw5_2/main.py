#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2

MAIN_PAGE_FOOTER_TEMPLATE = """
<form action="word-shuffle"><input type=text name=word1><br><input type=text name=word2><br><input type=submit value=Submit></form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(MAIN_PAGE_FOOTER_TEMPLATE)

class Result(webapp2.RequestHandler):
    def post(self):
        str1 = self.request.get('word1')
        str2 = self.request.get('word2')

        ans = ""
        str_len = max(len(str1), len(str2))
        for i in range(0, str_len):
            ans = ans + str1[i:i+1] + str2[i:i+1]

        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(ans)
        self.response.write('</pre></body></html>')
        
 

app = webapp2.WSGIApplication([
    ('/', MainPage),('/submit', Result)
], debug=True)
