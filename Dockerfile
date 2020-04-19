FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /app

RUN set -ex \
    && mkdir nvidia_git \
    && cd nvidia_git \
    && git clone https://github.com/NVIDIA/apex \
    && cd apex \
    && pip install -v --no-cache-dir ./ \
    && pip --no-cache-dir install --upgrade setuptools

COPY requirements.txt /app
RUN set -ex \
    && pip --no-cache-dir install -r /app/requirements.txt

COPY . /app
RUN set -ex \
    && pip --no-cache-dir install -e /app/

ENTRYPOINT ["python", "run.py"]