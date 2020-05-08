import os
import shutil
from core.common import logger, constants
from core.viz.common import html_initializer


def initialize_workdir():
    if not os.path.exists(constants.workdir_dirname):

        logger.log_task_init("creating directory '{}'".format(
            constants.workdir_dirname))

        os.makedirs(constants.workdir_dirname)

        logger.log_task_end("creating directory '{}'".format(
            constants.workdir_dirname))

    else:

        logger.log_message("directory '{}' already exists, removing it".format(
            constants.workdir_dirname))

        shutil.rmtree(constants.workdir_dirname)
        initialize_workdir()


def initialize_temporary_template_file():
    logger.log_task_init("creating file '{}'".format(
        constants.temporary_template_filepath))

    with open(constants.temporary_template_filepath, 'w+') as f:
        with open(constants.template_filename, 'r') as ifile:
            f.write(ifile.read())

    logger.log_task_end("creating file '{}'".format(
        constants.temporary_template_filepath))


app_prestart_initilizers = [
    initialize_workdir,
    initialize_temporary_template_file
]


def initialize():
    for app_prestart_initializer in app_prestart_initilizers:
        app_prestart_initializer()

    html_initializer.initialize()
