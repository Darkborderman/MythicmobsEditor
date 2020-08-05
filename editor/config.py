"""For service configuration"""
import os


class Config:
    MYTHICMOBS_FOLDER = os.environ.get("MYTHICMOBS_FOLDER", "./yml")
