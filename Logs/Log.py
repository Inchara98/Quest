import logging


from log_path import log_file_path


class log_details:

    @staticmethod
    def logen():
        _file = log_file_path()
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler(_file.get_log_file_dir() + '/status.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
