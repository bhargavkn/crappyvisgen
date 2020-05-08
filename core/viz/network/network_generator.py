import json
from string import Template
from core.common import logger, constants


def generate_network_html(div_id, nodes, edges):
    logger.log_task_init('generating html for network id={}'.format(div_id))

    nodes_str = json.dumps(nodes)
    edges_str = json.dumps(edges)

    logger.log_task_end('generating html for network id={}'.format(div_id))

    return nodes_str, edges_str


def add_network_to_template(div_id, nodes_str, edges_str):

    logger.log_task_init("adding network id={} to template".format(div_id))

    nodes_var_template_placeholder = \
        constants.network_js_nodes_var_template_placeholder.format(div_id)

    edges_var_template_placeholder = \
        constants.network_js_edges_var_template_placeholder.format(div_id)

    with open(constants.temporary_template_filepath, 'r') as f:
        html_template = Template(f.read())

    html_template_str = html_template.safe_substitute(
        {
            nodes_var_template_placeholder: nodes_str,
            edges_var_template_placeholder: edges_str,
            div_id: ""
        }
    )

    logger.log_task_end("adding network id={} to template".format(div_id))

    with open(constants.temporary_template_filepath, 'w') as f:
        f.write(html_template_str)