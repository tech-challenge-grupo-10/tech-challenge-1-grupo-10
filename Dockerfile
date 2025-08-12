FROM astral/uv:python3.12-bookworm-slim

WORKDIR /usr/src/app

COPY . .

RUN uv sync

CMD [ "uv", "run", "./main.py" ]
