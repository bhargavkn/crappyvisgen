import pandas as pd
from string import Template
from core.common import logger, constants


def generate_table_html(div_id, cols, rows, table_id=None, css_classes=None):
    logger.log_task_init('generating html for table id={}'.format(div_id))

    df = pd.DataFrame(rows, columns=cols)
    table_html_str = df.to_html(
        table_id=table_id,
        classes=css_classes,
        index=False,
        justify='left')

    logger.log_task_end('generating html for table id={}'.format(div_id))

    return table_html_str


def add_table_to_template(div_id, table_html_str):

    logger.log_task_init("adding table id={} to template".format(div_id))

    with open(constants.temporary_template_filepath, 'r') as f:
        html_template = Template(f.read())

    html_template_str = html_template.safe_substitute(
        {div_id: table_html_str}
    )

    with open(constants.temporary_template_filepath, 'w') as f:
        f.write(html_template_str)

    logger.log_task_end("adding table id={} to template".format(div_id))
