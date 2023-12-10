import re
from bs4 import BeautifulSoup


def extract_data(content, selector, parser="html.parser"):

    soup = BeautifulSoup(content, parser)
    peace = soup.select(selector)
    
    return peace

    """for tag in peace: # Das gehört in transform
        string_content = str(tag)

        if re.search(rule, string_content):
            match = re.search(rule, string_content)
            index_tuple = match.span()
            preresult = string_content[index_tuple[0]:index_tuple[1]]
            float_number = float(preresult.replace(".", "_").replace(",", "."))
            float_numbers.append(float_number)

    return float_number"""