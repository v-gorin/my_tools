def log_formater(src, indent=0, invert=False):
    """ Make log more readable and awesome
    The main application is using instead of json.dumps().
    :param src: dictionary with data, list of dicts

                Note: Indent for list by default is +3.
                If you wanna call log_formater for list,
                call it with indent=-3 for 0,
                indent=-3+1 for 1 and etc.
    :param indent: int
    :param invert: Swaps first and second columns. Can be used ONLY
     with one levels dictionary
    :return: formatted string with result, can be used in log
    """

    result = ''
    templates = ["\n{indent}{item:{len}}{value}" if not invert else
                 "\n{indent}{value:{len}}{item}",
                 "\n{indent}{item}:",
                 '\n{indent}{value}']

    if src and isinstance(src, dict):
        max_len = len(max(src.values() if invert else src.keys(),
                          key=lambda x: len(str(x))))
        for key, value in src.items():
            if (isinstance(value, dict) and value) or \
                    isinstance(value, list):
                result += templates[1].format(indent=' ' * indent,
                                              item=key)
                result += log_formater(value, indent + 3)
            else:
                result += templates[0].format(indent=' ' * indent,
                                              item=key,
                                              value=str(value),
                                              len=max_len + 5)

    elif src and isinstance(src, list):
        for el in src:
            if (isinstance(el, dict) and el) or isinstance(el, list):
                res = log_formater(el, indent + 3)
            else:
                res = templates[2].format(indent=' ' * (indent + 3),
                                          value=str(el))
            result += res[:indent + 2] + '-' + res[indent + 3:]
    return result


def main():
    """
    Usage examples
    """

    print(log_formater({'1': 'Test_1', '2': 'Test_2'}))
    print(log_formater({'1': 'Test_1', '2': 'Test_2'}, invert=True))

    big_json = {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para":
                                "A meta-markup language, used to create "
                                "markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]},
                        "GlossSee": "markup"}
                }
            }
        }
    }
    # Unreadable printing
    print(big_json)
    # Readable printing
    print log_formater(big_json)

if __name__ == '__main__':
    main()