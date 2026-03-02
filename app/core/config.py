from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # IBM i Database Connection
    IBMI_HOST: str = "172.20.20.38"
    IBMI_USER: str = "vp25-059-ibmi-9"
    IBMI_PASSWORD: str = "dPeT3e61"
    IBMI_DATABASE: str = "*LOCAL"
    IBMI_PORT: int = 446
    DB_DRIVER: str = "{IBM i Access ODBC Driver}"

    # Mock settings
    USE_MOCK: bool = True
    MOCK_DB_PATH: str = "data/mock/db2_mock.db"
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()