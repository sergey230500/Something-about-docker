FROM dimonpc2010/pytelegrambot

COPY  . /pythonbot

WORKDIR /pythonbot

EXPOSE 8001
RUN pip install pillow

CMD ["python" , "-u", "bot.py"]
