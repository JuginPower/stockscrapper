import requests


def download_data(urlString):

        """Return page source content from module requests or en errorstring."""
        error_string = ""

        try:
            page_source = requests.get(urlString)
        except requests.exceptions.RequestException as request_error:
            error_string += str(request_error)
        else:
            if not 200 <= page_source.status_code < 299:
                error_string += str(page_source.status_code)

            if len(error_string) == 0:
                return page_source.content

        return error_string
