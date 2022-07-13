# выбор базового образа https://hub.docker.com/_/python
FROM python:3.10.2-slim-bullseye as base
RUN pip3 install --no-cache-dir pandas nb_black notebook
RUN rm -rf /workspace
RUN mkdir /workspace
ENV WORKSPACE /workspace
WORKDIR $WORKSPACE
COPY migration.ipynb $WORKSPACE
COPY functions.ipynb $WORKSPACE
RUN mkdir $WORKSPACE/gitlab $WORKSPACE/gitlab/migration



# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD jupyter notebook \
   --no-browser \
   --port=8888 \
   --ip=0.0.0.0 \
   --allow-root \
   --NotebookApp.token='' \
   --NotebookApp.password=''

EXPOSE 8888