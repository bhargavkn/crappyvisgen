from core.common import constants
from string import Template
import core.common.logger as logger
from core.viz.common import html_utils


def initialize_datatable_scripts_for_html_table_rendering():
    logger.log_task_init("initializing datatable scripts")

    with open(constants.temporary_template_filepath, "r") as f:
        html_template = Template(f.read())

    datatable_init_js_scripts_str = ""

    with open(constants.temporary_template_filepath, 'r') as f:
        for line in f.readlines():
            result = constants.table_div_matcher_re.match(line)
            if result:
                div_id = html_utils.extract_id_from_html_elem(result.string)
                datatable_init_js_scripts_str += \
                    constants.datatable_declaration_js_script_tpl.format(div_id)

    html_template_str = html_template.safe_substitute(
        datatable_init_js_scripts=datatable_init_js_scripts_str
    )

    with open(constants.temporary_template_filepath, 'w') as f:
        logger.log_task_init("overwriting {} with datatable init js scripts".format(
            constants.temporary_template_filepath))

        f.write(html_template_str)

        logger.log_task_end("overwriting {} with datatable init js scripts".format(
            constants.temporary_template_filepath))

    logger.log_task_end("initializing datatable scripts")


def initialize_network_scripts():
    logger.log_task_init("initializing network js scripts")

    network_js_scripts_str = ""

    with open(constants.temporary_template_filepath, 'r') as f:
        html_template = Template(f.read())

    with open(constants.temporary_template_filepath, 'r') as f:
        for line in f.readlines():
            result = constants.network_div_matcher_re.match(line)
            if result:
                div_id = html_utils.extract_id_from_html_elem(result.string)
                network_js_scripts_str += constants.network_js_script_tpl.format(
                    div_id
                )

    html_template_str = html_template.safe_substitute(
        network_js_scripts=network_js_scripts_str
    )

    with open(constants.temporary_template_filepath, 'w') as f:
        logger.log_task_init("overwriting {} with network init js scripts".format(
            constants.temporary_template_filepath))

        f.write(html_template_str)

        logger.log_task_end("overwriting {} with network init js scripts".format(
            constants.temporary_template_filepath
        ))

    logger.log_task_end("initializing network js scripts")


# Add any new initializer function above this line, and add the function to the list of
# initializers below to get it executed at html page build time. Each element in the
# list below is a 2-tuple with the first element representing a brief message that will
# be logged as part of the initialization and the second element is the initializer
# method itself.
html_initializers = [
    initialize_datatable_scripts_for_html_table_rendering,
    initialize_network_scripts
]


def initialize():
    for initializer in html_initializers:
        initializer()
