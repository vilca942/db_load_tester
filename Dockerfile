FROM python:3.13-slim AS prebuild

# Build tools needed to build psycopg2 postgresql driver
RUN apt update && apt install -y gcc g++ git libpq-dev

RUN pip install --upgrade pip

RUN pip install "poetry>=2.0,<3.0" poetry-plugin-export

COPY pyproject.toml poetry.lock ./

RUN poetry export --without-hashes  -f requirements.txt --output requirements.txt

# Using wheel to build pip packages. This allows us to remove build
# dependencies like GCC from the final image. Everything is compiled here and
# then copied into the final image
RUN pip wheel -r ./requirements.txt --wheel-dir=./wheels

FROM python:3.13-slim

# Needed by fastapi to run webserver
RUN apt update && apt install -y libpq5

# Importing build wheels
COPY --from=prebuild /wheels ./wheels

# Installing dependencies
RUN pip install --no-cache-dir wheels/*.whl && rm -rf ./wheels

# Importing code
COPY src ./src

CMD ["fastapi", "run", "src/main.py", "--port", "5000"]
