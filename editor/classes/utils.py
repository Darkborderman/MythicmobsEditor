from typing import List

from loguru import logger

from lang import NAME_DICT, DESC_DICT


class MythicBase():

    def get_attributes(self) -> List[str]:
        """Get item's attributes"""
        return self.__dict__.keys()

    def get_name(self, attribute: str) -> str:
        """Get attribute name"""
        try:
            getattr(self, attribute)
            return NAME_DICT[attribute]
        except Exception as error:
            logger.info(error)
            return ''

    def get_desc(self, attribute: str) -> str:
        """Get attribute description"""
        try:
            getattr(self, attribute)
            return DESC_DICT[attribute]
        except Exception as error:
            logger.info(error)
            return ''
