import logging

logging.basicConfig(filename='filename.log', filemode='w', level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
