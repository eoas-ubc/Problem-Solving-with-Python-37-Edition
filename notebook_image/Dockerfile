FROM phaustin/base-image:sep15

USER root

RUN echo "change /home to jovyan" \
  && touch /home/pha_was_here \
  &&  chown -R ${NB_USER}:${NB_USER} /home \
  &&  chown -R ${NB_USER}:${NB_USER} /home/jovyan \
  && ls -ltd /* \
  && echo "finished chown"


COPY jupyter_notebook_config.py /etc/jupyter/ 
RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc \
  && mkdir -p  /home/jovyan/new_work \
  && chown -R ${NB_USER}:${NB_USER} /home/jovyan/new_work \
  && ls -ltd /home/jovyan/*

USER ${USER_NB}
WORKDIR ${HOME}
# CMD ["jupyterhub-singleuser"]
