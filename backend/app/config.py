from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration comes from environment variables (or a .env file)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://incident:incident@localhost:5432/incidentlog"

    jwt_secret: str = "change-me-in-env"
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = 60

    s3_bucket: str = "incidentlog-evidence"
    s3_region: str = "eu-west-2"
    s3_access_key: str | None = None
    s3_secret_key: str | None = None
    # Set for MinIO in local development; leave empty for real AWS S3.
    s3_endpoint_url: str | None = None
    # The address the BROWSER uses to reach storage (differs inside Docker).
    s3_public_endpoint_url: str | None = None
    max_upload_bytes: int = 10 * 1024 * 1024  # 10 MB

    cors_origins: list[str] = ["http://localhost:5173"]

    # Login protection
    max_failed_logins: int = 5
    lockout_minutes: int = 15
    login_rate_limit: str = "10/minute"  # per IP address
    mfa_issuer: str = "IncidentLog"


settings = Settings()