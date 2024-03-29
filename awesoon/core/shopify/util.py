import html
import re
from html.parser import HTMLParser
from io import StringIO


def decode_html_policies(policies):
    for policy in policies:
        policy["body"] = strip_tags(policy.get("body"))
    return policies


class MLStripper(HTMLParser):
    def __init__(self):
        """A markup language tag stripper class constructed from an html parser"""
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, data):
        self.text.write(html.unescape(data))

    def handle_starttag(self, tag, attrs):
        self.text.write(' ')
        
    def handle_endtag(self, tag):
        self.text.write(' ')

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    if not html:
        return ""
    s = MLStripper()
    s.feed(html)
    s.close()
    return re.sub(r'[\n\r\s]+', ' ', s.get_data())


def get_id_from_gid(uri):
    match = re.search(r"/(\d+)$", uri)
    if match:
        return match.group(1)
    return "-1"

