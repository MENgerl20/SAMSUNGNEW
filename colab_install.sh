#!/bin/bash

# Установка Buildozer и Cython (версия совместимая с Kivy)
pip install buildozer cython==0.29.33

# Обновление списка пакетов
sudo apt-get update

# Установка системных библиотек (максимальный набор для сборки)
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    autoconf \
    libtool \
    pkg-config \
    cmake
