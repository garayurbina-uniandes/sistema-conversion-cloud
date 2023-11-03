import os

# Get the PostgreSQL password from an environment variable
database_password = os.environ.get("DATABASE_PASSWORD")

# Check if the password is available, otherwise, provide a default
if not database_password:
    database_password = "your_default_password"

# Construct the SQLAlchemy Database URI
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{database_password}@mi-database-01.ciksrkbct7fm.us-east-1.rds.amazonaws.com:5432/conversorDB"
