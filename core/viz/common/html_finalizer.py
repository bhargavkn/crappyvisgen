import shutil
from core.common import logger, constants


def remove_workdir():
    logger.log_task_init("removing directory '{}'".format(constants.workdir_dirname))
    shutil.rmtree(constants.workdir_dirname)
    logger.log_task_end("removing directory '{}'".format(constants.workdir_dirname))


def create_final_html_file():
    logger.log_task_init(
        "storing finalized html in file={}".format(constants.output_filename))

    with open(constants.temporary_template_filepath) as f:
        html_str = f.read()

    with open(constants.output_filename, 'w+') as ofile:
        ofile.write(html_str)

    logger.log_task_end(
        "storing finalized html in file={}".format(constants.output_filename))


def finalize():
    create_final_html_file()
    remove_workdir()