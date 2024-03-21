from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.db.database import Base
from app.core.config import settings

from app.models.students import Students

config = context.config
DATABASE_URL = settings.DATABASE_URL


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


config.set_section_option(
    config.config_ini_section, "sqlalchemy.url", DATABASE_URL)


def run_migrations_offline() -> None:
   
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        compare_type=True,
        literal_binds=True,
        target_metadata=target_metadata,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
   
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            compare_type=True,
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
