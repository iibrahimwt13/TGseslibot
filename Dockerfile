FROM debian:latest

RUN apt update && apt upgrade -y
RUN sudo apt install pulseaudio mplayer pavucontrol screen
RUN bash pa.sh
RUN screen -S vcbot
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD python3 bot.py
