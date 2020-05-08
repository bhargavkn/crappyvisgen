from core.common import logger, constants


def extract_id_from_html_elem(html_elem_str):
    try:
        id_elem = constants.html_id_matcher_re.findall(html_elem_str)[0]
        id_elem = id_elem.replace("id=", "")
        id_elem = id_elem.replace("\"", "")
        return id_elem

    except:
        logger.log_error("error while extracting id from elem: {}".format(
            html_elem_str.strip()))
        exit(1)
