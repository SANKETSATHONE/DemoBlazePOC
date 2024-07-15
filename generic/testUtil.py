import logging
from generic.fileFunctionUtil import FileFunctionUtil
import datetime

class TestUtil:

    logger = None
    @staticmethod
    def get_logger():

        TestUtil.logger = logging.getLogger()
        TestUtil.logger.setLevel(logging.INFO)

        fileName = datetime.datetime.strftime(datetime.datetime.now(),"%d_%m_%y_%H_%M_%S_%f")
        logPath = FileFunctionUtil.get_dynamic_path("DemoBlazePOC") + "\\report\\"+f"{fileName}.log"

        handler = logging.FileHandler(logPath, mode="w")
        logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")

        handler.setFormatter(logFormatter)
        TestUtil.logger.addHandler(handler)




