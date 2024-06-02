FROM python:3.9
ARG APP_VERSION
ENV VERSION=$APP_VERSION
COPY dist/patternlib-$VERSION-py3-none-any.whl /root/patternlib-$VERSION-py3-none-any.whl
RUN pip install -U pip 
RUN pip install /root/patternlib-$VERSION-py3-none-any.whl
COPY eg.py /root/eg.py
ENTRYPOINT ["python", "/root/eg.py"]
CMD ["--list"]
