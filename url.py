import socket


class URL:
    def __init__(self, url):
        # separate scheme from rest of url
        self.scheme, url = url.split("://", 1)
        assert self.scheme == "http"

        # separate the host from the path
        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" + url

    def request(self):
        # create a socket
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP,
        )

        # connect to the other computer
        # host and port needed
        s.connect((self.host, 80))

        # form the HTTP request
        request = f"GET {self.path} HTTP/1.0\r\n"
        request += f"Host: {self.host}\r\n"
        request += "\r\n"

        # send the HTTP request
        s.send(request.encode("utf8"))
