#!/usr/bin/env bash

# Nginx에 존재하던 모든 enabled서버 설정 링크 삭제
sudo rm -rf /etc/nginx/sites-enabled/*
# 프로젝트의 Nginx설정 (nginx-app.conf)를 복사
sudo cp -f /srv/ec2-deploy/.config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
# 복사한 Nginx설정을 enabled에 링크
sudo ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
# uWSGI서비스 파일을 /etc/systemd/system폴더에 복사
#sudo cp -f /srv/ec2-deploy/.config/uwsgi/uwsgi.service /etc/systemd/system/uwsgi.service
sudo cp -f /srv/ec2-deploy/.config/uwsgi/uwsgi-dev.service /etc/systemd/system/uwsgi-dev.service


##  collectstatic을 위한 과정  ##

# 3/6 수업시간 추가
# https://youtu.be/rlmKMVOStbU?t=43m51s
export DJANGO_SETTINGS_MODULE=config.settings.dev

cd /srv/ec2-deploy/app
# ubuntu유저로 collectstatic명령어를 실행 (deploy스크립트가 root권한으로 실행되므로)
/bin/bash -c '/home/ubuntu/.pyenv/versions/fc-ec2-deploy/bin/python \
/srv/ec2-deploy/app/manage.py collectstatic --noinput' ubuntu

# uwsgi-dev, nginx를 재시작 (uwsgi는 stop)
sudo systemctl stop uwsgi # -> 동일한 socket을 쓰면 이 과정이 사실 의미 없긴 함..
sudo systemctl enable uwsgi-dev
sudo systemctl daemon-reload
sudo systemctl restart uwsgi-dev nginx
