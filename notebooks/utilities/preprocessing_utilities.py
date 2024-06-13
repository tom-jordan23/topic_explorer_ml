import re
from textacy import preprocessing



def simple_string_preprocessing(text):
    if isinstance(text, str) == False:
        return None

    # remove square brackets but leave the content
    # sample = """On 11 March, a team of WHO staff and partners [delivered](https://ochaopt.us5.list-"""
    text = text.replace("[", " ")
    text = text.replace("]", " ")

    # for now remove parentheticals, but there is valuable content in there
    # they serve multiple functions though so that needs to be addressed
    text = preprocessing.remove.brackets(text)

    # convert 3-4 to '3 to 4' ... important to that it doesn't
    # inadvertently become 34
    pattern = r'(\d+)-(\d+)'

    def replace_match(match):
        return f"{match.group(1)} to {match.group(2)}"

    text = re.sub(pattern, replace_match, text)

    # replace so tokenization doesn't separate
    text = text.replace("-", "")

    text = preprocessing.replace.urls(text, "")
    text = preprocessing.replace.emails(text, "")

    # remove all non alpha numeric and punctuation
    pattern = r'[^a-zA-Z0-9\s\,\.\?\!\(\)\%\:\_]'
    text = re.sub(pattern, '', text)

    text = text.replace("\n","")
    text = preprocessing.normalize.whitespace(text)
    return text


def numeric_string_preprocessing(text):
    if isinstance(text, str) == False:
        return None

    text = text.replace("per cent","percent")
    text = text.replace("%"," percent")

    text = text.replace(" km "," kilometers ")
    text = text.replace("%"," percent")


    #text = re.sub(pattern, ' kilometers', text)
    def replace_match(match):
        return f"{match.group(1)} kilometers"
    text = re.sub(r'(\d)(\s?)(km)', replace_match, text)


    text = preprocessing.normalize.whitespace(text)

    return text
