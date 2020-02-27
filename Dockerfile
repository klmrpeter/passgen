FROM python:3
ADD pg.py /
ENTRYPOINT ["python", "pg.py"]
CMD ["-s 20", "-f", "-u", "-c", "-k"]
