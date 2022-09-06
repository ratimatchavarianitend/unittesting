import os

ENVIRONMENT = os.get()


class Environments(Enum):
    DEBUG = "DEBUG"
    DEVELOP = "DEVELOP"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"
    INTEGRATION = "INTEGRATION"


IS_INTEGRATION_ENVIRONMENT = ENVIRONMENT == Environments.INTEGRATION
